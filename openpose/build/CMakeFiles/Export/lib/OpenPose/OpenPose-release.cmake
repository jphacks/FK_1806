#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "openpose_3d" for configuration "Release"
set_property(TARGET openpose_3d APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_3d PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "caffe;openpose_core"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_3d.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_3d.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_3d )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_3d "${_IMPORT_PREFIX}/lib/libopenpose_3d.dylib" )

# Import target "openpose_calibration" for configuration "Release"
set_property(TARGET openpose_calibration APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_calibration PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose_core"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_calibration.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_calibration.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_calibration )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_calibration "${_IMPORT_PREFIX}/lib/libopenpose_calibration.dylib" )

# Import target "openpose_core" for configuration "Release"
set_property(TARGET openpose_core APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_core PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose;caffe;opencv_calib3d;opencv_core;opencv_dnn;opencv_features2d;opencv_flann;opencv_highgui;opencv_imgcodecs;opencv_imgproc;opencv_ml;opencv_objdetect;opencv_photo;opencv_shape;opencv_stitching;opencv_superres;opencv_video;opencv_videoio;opencv_videostab;opencv_aruco;opencv_bgsegm;opencv_bioinspired;opencv_ccalib;opencv_datasets;opencv_dnn_objdetect;opencv_dpm;opencv_face;opencv_fuzzy;opencv_hfs;opencv_img_hash;opencv_line_descriptor;opencv_optflow;opencv_phase_unwrapping;opencv_plot;opencv_reg;opencv_rgbd;opencv_saliency;opencv_stereo;opencv_structured_light;opencv_surface_matching;opencv_tracking;opencv_xfeatures2d;opencv_ximgproc;opencv_xobjdetect;opencv_xphoto;/usr/local/lib/libcaffe.dylib;/usr/local/lib/libglog.dylib;opencv_calib3d;opencv_core;opencv_dnn;opencv_features2d;opencv_flann;opencv_highgui;opencv_imgcodecs;opencv_imgproc;opencv_ml;opencv_objdetect;opencv_photo;opencv_shape;opencv_stitching;opencv_superres;opencv_video;opencv_videoio;opencv_videostab;opencv_aruco;opencv_bgsegm;opencv_bioinspired;opencv_ccalib;opencv_datasets;opencv_dnn_objdetect;opencv_dpm;opencv_face;opencv_fuzzy;opencv_hfs;opencv_img_hash;opencv_line_descriptor;opencv_optflow;opencv_phase_unwrapping;opencv_plot;opencv_reg;opencv_rgbd;opencv_saliency;opencv_stereo;opencv_structured_light;opencv_surface_matching;opencv_tracking;opencv_xfeatures2d;opencv_ximgproc;opencv_xobjdetect;opencv_xphoto;/usr/local/lib/libcaffe.dylib;/usr/local/lib/libgflags.dylib;/usr/local/lib/libglog.dylib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_core.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_core.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_core )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_core "${_IMPORT_PREFIX}/lib/libopenpose_core.dylib" )

# Import target "openpose_face" for configuration "Release"
set_property(TARGET openpose_face APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_face PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose_core"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_face.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_face.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_face )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_face "${_IMPORT_PREFIX}/lib/libopenpose_face.dylib" )

# Import target "openpose_filestream" for configuration "Release"
set_property(TARGET openpose_filestream APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_filestream PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose_core"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_filestream.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_filestream.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_filestream )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_filestream "${_IMPORT_PREFIX}/lib/libopenpose_filestream.dylib" )

# Import target "openpose_gpu" for configuration "Release"
set_property(TARGET openpose_gpu APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_gpu PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose_core"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_gpu.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_gpu.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_gpu )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_gpu "${_IMPORT_PREFIX}/lib/libopenpose_gpu.dylib" )

# Import target "openpose_gui" for configuration "Release"
set_property(TARGET openpose_gui APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_gui PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose_pose;opencv_calib3d;opencv_core;opencv_dnn;opencv_features2d;opencv_flann;opencv_highgui;opencv_imgcodecs;opencv_imgproc;opencv_ml;opencv_objdetect;opencv_photo;opencv_shape;opencv_stitching;opencv_superres;opencv_video;opencv_videoio;opencv_videostab;opencv_aruco;opencv_bgsegm;opencv_bioinspired;opencv_ccalib;opencv_datasets;opencv_dnn_objdetect;opencv_dpm;opencv_face;opencv_fuzzy;opencv_hfs;opencv_img_hash;opencv_line_descriptor;opencv_optflow;opencv_phase_unwrapping;opencv_plot;opencv_reg;opencv_rgbd;opencv_saliency;opencv_stereo;opencv_structured_light;opencv_surface_matching;opencv_tracking;opencv_xfeatures2d;opencv_ximgproc;opencv_xobjdetect;opencv_xphoto"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_gui.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_gui.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_gui )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_gui "${_IMPORT_PREFIX}/lib/libopenpose_gui.dylib" )

# Import target "openpose_hand" for configuration "Release"
set_property(TARGET openpose_hand APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_hand PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose_core"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_hand.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_hand.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_hand )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_hand "${_IMPORT_PREFIX}/lib/libopenpose_hand.dylib" )

# Import target "openpose_net" for configuration "Release"
set_property(TARGET openpose_net APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_net PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "caffe;openpose_core"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_net.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_net.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_net )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_net "${_IMPORT_PREFIX}/lib/libopenpose_net.dylib" )

# Import target "openpose_pose" for configuration "Release"
set_property(TARGET openpose_pose APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_pose PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose_core"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_pose.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_pose.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_pose )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_pose "${_IMPORT_PREFIX}/lib/libopenpose_pose.dylib" )

# Import target "openpose_producer" for configuration "Release"
set_property(TARGET openpose_producer APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_producer PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "opencv_calib3d;opencv_core;opencv_dnn;opencv_features2d;opencv_flann;opencv_highgui;opencv_imgcodecs;opencv_imgproc;opencv_ml;opencv_objdetect;opencv_photo;opencv_shape;opencv_stitching;opencv_superres;opencv_video;opencv_videoio;opencv_videostab;opencv_aruco;opencv_bgsegm;opencv_bioinspired;opencv_ccalib;opencv_datasets;opencv_dnn_objdetect;opencv_dpm;opencv_face;opencv_fuzzy;opencv_hfs;opencv_img_hash;opencv_line_descriptor;opencv_optflow;opencv_phase_unwrapping;opencv_plot;opencv_reg;opencv_rgbd;opencv_saliency;opencv_stereo;opencv_structured_light;opencv_surface_matching;opencv_tracking;opencv_xfeatures2d;opencv_ximgproc;opencv_xobjdetect;opencv_xphoto;openpose_core;openpose_thread;openpose_filestream"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_producer.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_producer.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_producer )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_producer "${_IMPORT_PREFIX}/lib/libopenpose_producer.dylib" )

# Import target "openpose_thread" for configuration "Release"
set_property(TARGET openpose_thread APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_thread PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose_core"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_thread.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_thread.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_thread )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_thread "${_IMPORT_PREFIX}/lib/libopenpose_thread.dylib" )

# Import target "openpose_tracking" for configuration "Release"
set_property(TARGET openpose_tracking APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_tracking PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose_core"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_tracking.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_tracking.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_tracking )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_tracking "${_IMPORT_PREFIX}/lib/libopenpose_tracking.dylib" )

# Import target "openpose_utilities" for configuration "Release"
set_property(TARGET openpose_utilities APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_utilities PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose_producer;openpose_filestream"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_utilities.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_utilities.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_utilities )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_utilities "${_IMPORT_PREFIX}/lib/libopenpose_utilities.dylib" )

# Import target "openpose_wrapper" for configuration "Release"
set_property(TARGET openpose_wrapper APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose_wrapper PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "openpose_thread;openpose_pose;openpose_hand;openpose_core;openpose_face;openpose_filestream;openpose_gui;openpose_producer;openpose_utilities"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose_wrapper.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose_wrapper.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose_wrapper )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose_wrapper "${_IMPORT_PREFIX}/lib/libopenpose_wrapper.dylib" )

# Import target "openpose" for configuration "Release"
set_property(TARGET openpose APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openpose PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "opencv_calib3d;opencv_core;opencv_dnn;opencv_features2d;opencv_flann;opencv_highgui;opencv_imgcodecs;opencv_imgproc;opencv_ml;opencv_objdetect;opencv_photo;opencv_shape;opencv_stitching;opencv_superres;opencv_video;opencv_videoio;opencv_videostab;opencv_aruco;opencv_bgsegm;opencv_bioinspired;opencv_ccalib;opencv_datasets;opencv_dnn_objdetect;opencv_dpm;opencv_face;opencv_fuzzy;opencv_hfs;opencv_img_hash;opencv_line_descriptor;opencv_optflow;opencv_phase_unwrapping;opencv_plot;opencv_reg;opencv_rgbd;opencv_saliency;opencv_stereo;opencv_structured_light;opencv_surface_matching;opencv_tracking;opencv_xfeatures2d;opencv_ximgproc;opencv_xobjdetect;opencv_xphoto;/usr/local/lib/libglog.dylib;/usr/local/lib/libglog.dylib;/usr/local/lib/libcaffe.dylib;/usr/local/lib/libgflags.dylib;pthread;caffe"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenpose.1.4.0.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libopenpose.1.4.0.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openpose )
list(APPEND _IMPORT_CHECK_FILES_FOR_openpose "${_IMPORT_PREFIX}/lib/libopenpose.1.4.0.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
