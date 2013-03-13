#
#  static_library.gypi
#
#  Created by Taihyun Hwang on 13/Mar/13.
#  Copyright (c) 2013 xenosoz. All rights reserved.
#
{
  'conditions': [
    [
      'OS=="ios"', {
        'includes': [
          'iphoneos-static_library/iphoneos-static_library.gypi',
        ],
      },
    ],
  ],
}
