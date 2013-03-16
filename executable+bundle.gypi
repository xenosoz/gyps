#
#  executable+bundle.gypi
#
#  Created by Taihyun Hwang on 16/Mar/13.
#  Copyright (c) 2013 xenosoz. All rights reserved.
#
{
  'conditions': [
    [
      'OS=="ios"', {
        'includes': [
          'iphoneos-executable+bundle/iphoneos-executable+bundle.gypi',
        ],
      },
    ],
  ],
}
