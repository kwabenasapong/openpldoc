 ; Place the script in your gimp scripts folder (eg. ~/.gimp-2.8/scripts) go to the
 ; folder with images you wish to round corners on and execute like this:
 ; gimp --no-data -i -b '(round-top-corners "*.png")' -b '(gimp-quit 0)'
 ;

 (define (round-top-corners pattern)
   (let* ((filelist (cadr (file-glob pattern 1))))
     (while (not (null? filelist))
       (let* ((filename (car filelist))
         (image (car (gimp-file-load RUN-NONINTERACTIVE filename filename)))
         (width (car (gimp-image-width image)))
         (drawable (car (gimp-image-get-active-layer image))))
         ; select 6 pixels in the top left corner and clear them
         (gimp-rect-select image 0 0 2 2 REPLACE 0 0)
         (gimp-rect-select image 0 2 1 1 ADD 0 0)
         (gimp-rect-select image 2 0 1 1 ADD 0 0)
         (define cornerselectionleft (car (gimp-image-active-drawable image)))
         (gimp-edit-clear cornerselectionleft)
         ; select 6 pixels in the top right corner and clear them
         (gimp-rect-select image (- width 2) 0 2 2 REPLACE 0 0)
         (gimp-rect-select image (- width 3) 0 1 1 ADD 0 0)
         (gimp-rect-select image (- width 1) 2 1 1 ADD 0 0)
         (define cornerselectionright (car (gimp-image-active-drawable image)))
         (gimp-edit-clear cornerselectionright)
         (set! drawable (car (gimp-image-merge-visible-layers image 0)))
         (gimp-file-save RUN-NONINTERACTIVE image drawable filename filename)
         (gimp-image-delete image)
       )
       (set! filelist (cdr filelist))
     )
   )
 )
