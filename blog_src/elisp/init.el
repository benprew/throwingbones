(require 'ox-publish)

(setq org-export-with-sub-superscripts nil)
(setq org-use-sub-superscripts nil)

(add-to-list 'load-path (file-name-directory load-file-name))
(require 'blog-tags)

;; Customize the HTML output
(setq org-html-validation-link nil            ;; Don't show validation link
      org-html-head-include-scripts nil       ;; Use our own scripts
      org-html-head-include-default-style nil ;; Use our own styles
      org-html-head "<link rel=\"stylesheet\" href=\"style.css\" />")

;; Hook into publishing pipeline
;; Generate tag pages and index after publishing is done
(defun my-blog-after-publish (&rest args)
  "Generate tag pages and index after all publishing is complete."
  (let ((org-dir "~/src/throwingbones/blog_src/org")
        (pub-dir "~/src/throwingbones/ben/blog"))
    ;; Clear and repopulate hash tables by scanning all org files recursively
    (clrhash my-blog-tags-table)
    (clrhash my-blog-posts-table)
    (dolist (file (directory-files-recursively org-dir "\\.org$"))
      (my-blog-collect-tags file pub-dir))
    ;; Generate tag pages and index
    (my-blog-generate-tag-pages pub-dir)
    (my-blog-generate-index-page pub-dir)))

;; Add advice to org-publish-all to run tag generation after publishing
(advice-add 'org-publish-all :after #'my-blog-after-publish)

(add-to-list 'org-export-filter-final-output-functions
             #'my-blog-fix-stylesheet-path)
(add-to-list 'org-export-filter-final-output-functions
             #'my-blog-insert-tags)

;; Org-publish project definition
(setq org-publish-project-alist
      '(("blog-org"
         :base-directory "~/src/throwingbones/blog_src/org"
         :publishing-directory "~/src/throwingbones/ben/blog"
         :recursive t
         :publishing-function org-html-publish-to-html
         :with-author t
         :with-creator nil
         :with-toc nil
         :section-numbers nil
         :time-stamp-file nil
         :html-head-include-default-style nil
         :html-head "<link rel=\"stylesheet\" href=\"style.css\"/>")

        ("blog-static"
         :base-directory "~/src/throwingbones/blog_src/org"
         :base-extension "css\\|js\\|png\\|jpg\\|gif"
         :publishing-directory "~/src/throwingbones/ben/blog"
         :recursive t
         :publishing-function org-publish-attachment)

        ("blog" :components ("blog-org" "blog-static"))))


;; (progn (clrhashmy-blog-tags-table)
;;        (clrhash my-blog-posts-table)
;;        (dolist (file (directory-files \"~/blog/org\" t \"\\.org$\"))(my-blog-collect-tags file \"~/blog/public\")) (my-blog-generate-tag-pages\"~/blog/public\") (my-blog-generate-index-page \"~/blog/public\"))
