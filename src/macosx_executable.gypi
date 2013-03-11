#
#  macosx_executable.gypi
#
#  Created by Taihyun Hwang on 11/Mar/13.
#  Copyright (c) xenosoz. All right reserved.
#
{
  'type': 'executable',
  'configurations': {
    'Debug': {
      'xcode_settings': {
        'ALWAYS_SEARCH_USER_PATHS': 'NO',
        'ARCHS': '$(ARCHS_STANDARD_32_64_BIT)',
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
        'MACOSX_DEPLOYMENT_TARGET': '10.8',
        'ONLY_ACTIVE_ARCH': 'YES',
        'SDKROOT': 'macosx',
        # Example per project settings.
        #'COMBINE_HIDPI_IMAGES': 'YES',
        #'GCC_PRECOMPILE_PREFIX_HEADER': 'YES',
        #'GCC_PREFIX_HEADER': "test-Prefix.pch',
        #'INFOPLIST_FILE': 'test-Info.plist',
        #'PRODUCT_NAME': '$(TARGET_NAME)',
        #'WRAPPER_EXTENSION': 'app',
      },
    },
    'Release': {
      'xcode_settings': {
        'ALWAYS_SEARCH_USER_PATHS': 'NO',
        'ARCHS': '$(ARCHS_STANDARD_32_64_BIT)',
        'CLANG_CXX_LANGUAGE_STANDARD': 'gnu++0x',
        'CLANG_CXX_LIBRARY': 'libc++',
        'CLANG_WARN_CONSTANT_CONVERSION': 'YES',
        'CLANG_WARN_EMPTY_BODY': 'YES',
        'CLANG_WARN_ENUM_CONVERSION': 'YES',
        'CLANG_WARN_INT_CONVERSION': 'YES',
        'CLANG_WARN__DUPLICATE_METHOD_MATCH': 'YES',
        'COPY_PHASE_STRIP': 'YES',
        'DEBUG_INFORMATION_FORMAT': 'dwarf-with-dsym',
        'GCC_C_LANGUAGE_STANDARD': 'gnu99',
        'GCC_ENABLE_OBJC_EXCEPTIONS': 'YES',
        'GCC_WARN_64_TO_32_BIT_CONVERSION': 'YES',
        'GCC_WARN_ABOUT_RETURN_TYPE': 'YES',
        'GCC_WARN_UNINITIALIZED_AUTOS': 'YES',
        'GCC_WARN_UNUSED_VARIABLE': 'YES',
        'MACOSX_DEPLOYMENT_TARGET': '10.8',
        'SDKROOT': 'macosx',
        # Example per project settings.
        #'COMBINE_HIDPI_IMAGES': 'YES',
        #'GCC_PRECOMPILE_PREFIX_HEADER': 'YES',
        #'GCC_PREFIX_HEADER': 'test-Prefix.pch',
        #'INFOPLIST_FILE': 'test-Info.plist',
        #'PRODUCT_NAME': '$(TARGET_NAME)',
        #'WRAPPER_EXTENSION': 'app',
      },
    },
  },
  'link_settings': {
    'libraries': [
      '$(SDKROOT)/System/Library/Frameworks/Cocoa.framework',
    ],
  }
}
