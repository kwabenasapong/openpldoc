 ; Based on script by Michiel Roos, found on:
 ; http://www.typofree.org/article/archive/2009/january/title/create-a-drop-shadow-folder-action/
 ;
 ; Place the script in your gimp scripts folder (eg. ~/.gimp-2.8/scripts) go to the
 ; folder with images you wish to add shadow to and execute like this:
 ; gimp --no-data -i -b '(batch-drop-shadow "*.png" 8 8 10)' -b '(gimp-quit 0)'
 ;

 (define (batch-drop-shadow pattern 
                             offsetx
                             offsety
                             radius)
   (let* ((filelist (cadr (file-glob pattern 1))))
     (while (not (null? filelist))
       (let* ((filename (car filelist))
         (image (car (gimp-file-load RUN-NONINTERACTIVE filename filename)))
         (drawable (car (gimp-image-get-active-layer image))))
         (script-fu-drop-shadow image drawable offsetx offsety radius '(0 0 0) 80.0 TRUE)
         (set! drawable (car (gimp-image-merge-visible-layers image 0)))
         (gimp-file-save RUN-NONINTERACTIVE image drawable filename filename)
         (gimp-image-delete image)
       )
       (set! filelist (cdr filelist))
     )
   )
 )
