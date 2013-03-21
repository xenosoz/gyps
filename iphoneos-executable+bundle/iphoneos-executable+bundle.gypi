#
#  iphoneos_executable+bundle.gypi
#
#  Created by Taihyun Hwang on 16/Mar/13.
#  Copyright (c) xenosoz. All right reserved.
#
{
  'type': 'executable',
  'mac_bundle': 1,
  'configurations': {
    'Debug': {
      'xcode_settings': {
        'ALWAYS_SEARCH_USER_PATHS': 'NO',
        'ARCHS': '$(ARCHS_STANDARD_32_BIT)',
        'OTHER_LDFLAGS': [
          '-ObjC',
        ],
        'CLANG_CXX_LANGUAGE_STANDARD': 'gnu++0x',
        'CLANG_CXX_LIBRARY': 'libc++',
        'CLANG_WARN_CONSTANT_CONVERSION': 'YES',
        'CLANG_WARN_EMPTY_BODY': 'YES',
        'CLANG_WARN_ENUM_CONVERSION': 'YES',
        'CLANG_WARN_INT_CONVERSION': 'YES',
        'CLANG_WARN__DUPLICATE_METHOD_MATCH': 'YES',
        'COPY_PHASE_STRIP': 'NO',
        'GCC_C_LANGUAGE_STANDARD': 'gnu99',
        'GCC_DYNAMIC_NO_PIC': 'NO',
        'GCC_ENABLE_OBJC_EXCEPTIONS': 'YES',
        'GCC_OPTIMIZATION_LEVEL': '0',
        'GCC_PREPROCESSOR_DEFINITIONS': [
          'DEBUG=1',
          '$(inherited)',
        ],
        'GCC_SYMBOLS_PRIVATE_EXTERN': 'NO',
        'GCC_WARN_64_TO_32_BIT_CONVERSION': 'YES',
        'GCC_WARN_ABOUT_RETURN_TYPE': 'YES',
        'GCC_WARN_UNINITIALIZED_AUTOS': 'YES',
        'GCC_WARN_UNUSED_VARIABLE': 'YES',
        'IPHONEOS_DEPLOYMENT_TARGET': '5.1',
        'ONLY_ACTIVE_ARCH': 'YES',
        'SDKROOT': 'iphoneos',
        # Example per project settings.
        #'TARGETED_DEVICE_FAMILY': '1,2',
        #'CODE_SIGN_IDENTITY': 'iPhone Developer',
        #'COMBINE_HIDPI_IMAGES': 'YES',
        #'GCC_PRECOMPILE_PREFIX_HEADER': 'YES',
        #'GCC_PREFIX_HEADER': 'test-Prefix.pch',
        #'INFOPLIST_FILE': 'test-Info.plist',
        #'PRODUCT_NAME': '$(TARGET_NAME)',
      },
    },
    'Release': {
      'xcode_settings': {
        'ALWAYS_SEARCH_USER_PATHS': 'NO',
        'ARCHS': '$(ARCHS_STANDARD_32_BIT)',
        'OTHER_CFLAGS': [
          '-DNS_BLOCK_ASSERTIONS',
        ],
        'OTHER_LDFLAGS': [
          '-ObjC',
        ],
        'CLANG_CXX_LANGUAGE_STANDARD': 'gnu++0x',
        'CLANG_CXX_LIBRARY': 'libc++',
        'CLANG_WARN_CONSTANT_CONVERSION': 'YES',
        'CLANG_WARN_EMPTY_BODY': 'YES',
        'CLANG_WARN_ENUM_CONVERSION': 'YES',
        'CLANG_WARN_INT_CONVERSION': 'YES',
        'CLANG_WARN__DUPLICATE_METHOD_MATCH': 'YES',
        'VALIDATE_PRODUCT': 'YES',
        'COPY_PHASE_STRIP': 'YES',
        'DEBUG_INFORMATION_FORMAT': 'dwarf-with-dsym',
        'GCC_C_LANGUAGE_STANDARD': 'gnu99',
        'GCC_ENABLE_OBJC_EXCEPTIONS': 'YES',
        'GCC_WARN_64_TO_32_BIT_CONVERSION': 'YES',
        'GCC_WARN_ABOUT_RETURN_TYPE': 'YES',
        'GCC_WARN_UNINITIALIZED_AUTOS': 'YES',
        'GCC_WARN_UNUSED_VARIABLE': 'YES',
        'IPHONEOS_DEPLOYMENT_TARGET': '5.1',
        'SDKROOT': 'iphoneos',
        # Example per project settings.
        #'TARGETED_DEVICE_FAMILY': '1,2',
        #'CODE_SIGN_IDENTITY': 'iPhone Developer',
        #'COMBINE_HIDPI_IMAGES': 'YES',
        #'GCC_UNROLL_LOOPS': 'YES',
        #'GCC_PRECOMPILE_PREFIX_HEADER': 'YES',
        #'GCC_PREFIX_HEADER': 'test-Prefix.pch',
        #'INFOPLIST_FILE': 'test-Info.plist',
        #'PRODUCT_NAME': '$(TARGET_NAME)',
      },
    },
  },
  'link_settings': {
    'libraries': [
      '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
      '$(SDKROOT)/System/Library/Frameworks/UIKit.framework',
      '$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework',
      '$(SDKROOT)/System/Library/Frameworks/QuartzCore.framework',
    ],
  }
}
