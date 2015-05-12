%module OpenCC
%{
#include "OpenCC/src/opencc.h"
%}

#define OPENCC_DEFAULT_CONFIG_SIMP_TO_TRAD "s2t.json"
#define OPENCC_DEFAULT_CONFIG_TRAD_TO_SIMP "t2s.json"

opencc_t opencc_open(const char*);

int opencc_close(opencc_t);

char* opencc_convert_utf8(opencc_t,
                          const char*,
                          size_t);

const char* opencc_error(void);
