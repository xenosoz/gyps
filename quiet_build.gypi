#
#  quiet_build.gypi
#
#  Created by Taihyun Hwang on 13/Mar/13.
#  Copyright (c) 2013 xenosoz. All rights reserved.
#
{
  'conditions': [
    [
      'OS=="ios"', {
        'includes': [
          'iphoneos-quiet_build/iphoneos-quiet_build.gypi',
        ],
      },
    ],
  ],
}
