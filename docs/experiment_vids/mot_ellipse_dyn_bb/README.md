## Multi-Object Tracking


#### experiment MOT + ellipse + dynamic_bb

![mot_ellipse_dyn_bb.gif](./gifs/mot_ellipse_dyn_bb.gif)

Controller is turned off. We start with three targets to track through occlusions. One of them performing lane changing maneuvers while the other two following a straight path. Parameters of the enclosing ellipse is computed and displayed in the tracking window.
For robustness in recovery through prolonged occlusions bounding box sizes are varied according to covariance in estimation.



