//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetatype.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, rituals for functions the generator leaves out: 4. Kept as it is
//  when the generator runs again.
#include <QtCore/qmetatype.h>

//  bool QtPrivate::QTypeNormalizer::is_ident_char(char s)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate15QTypeNormalizer13is_ident_charEc(char s) {
  return QtPrivate::QTypeNormalizer::is_ident_char(s);
}

//  bool QtPrivate::QTypeNormalizer::is_space(char s)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate15QTypeNormalizer8is_spaceEc(char s) {
  return QtPrivate::QTypeNormalizer::is_space(s);
}

//  bool QtPrivate::QTypeNormalizer::is_number(char s)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate15QTypeNormalizer9is_numberEc(char s) {
  return QtPrivate::QTypeNormalizer::is_number(s);
}

//  bool QtPrivate::QTypeNormalizer::starts_with_token(const char *b, const
//      char *e, const char *token, bool msvcKw)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate15QTypeNormalizer17starts_with_tokenEPKcS2_S2_b(
    const char *b,
    const char *e,
    const char *token,
    bool msvcKw) {
  return QtPrivate::QTypeNormalizer::starts_with_token(b, e, token, msvcKw);
}

//  const char *QtPrivate::QTypeNormalizer::skipString(const char *x, const
//      char *e)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN9QtPrivate15QTypeNormalizer10skipStringEPKcS2_(
    const char *x,
    const char *e) {
  return QtPrivate::QTypeNormalizer::skipString(x, e);
}

//  const char *QtPrivate::QTypeNormalizer::skipTemplate(const char *x, const
//      char *e, bool stopAtComa)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN9QtPrivate15QTypeNormalizer12skipTemplateEPKcS2_b(
    const char *x,
    const char *e,
    bool stopAtComa) {
  return QtPrivate::QTypeNormalizer::skipTemplate(x, e, stopAtComa);
}

//  void QtPrivate::QTypeNormalizer::append(char x)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QTypeNormalizer6appendEc(
    QtPrivate::QTypeNormalizer *self,
    char x) {
  self->append(x);
}

//  void QtPrivate::QTypeNormalizer::replaceLast(char x)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QTypeNormalizer11replaceLastEc(
    QtPrivate::QTypeNormalizer *self,
    char x) {
  self->replaceLast(x);
}

//  void QtPrivate::QTypeNormalizer::appendStr(const char *x)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QTypeNormalizer9appendStrEPKc(
    QtPrivate::QTypeNormalizer *self,
    const char *x) {
  self->appendStr(x);
}

#if defined(Q_CC_CLANG) || defined (Q_CC_GNU)
//  int QtPrivate::QTypeNormalizer::normalizeTypeFromSignature(const char
//      *begin, const char *end)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15QTypeNormalizer26normalizeTypeFromSignatureEPKcS2_(
    QtPrivate::QTypeNormalizer *self,
    const char *begin,
    const char *end) {
  return self->normalizeTypeFromSignature(begin, end);
}
#endif  // defined(Q_CC_CLANG) || defined (Q_CC_GNU)

//  int QtPrivate::QTypeNormalizer::normalizeType(const char *begin, const
//      char *end, bool adjustConst)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15QTypeNormalizer13normalizeTypeEPKcS2_b(
    QtPrivate::QTypeNormalizer *self,
    const char *begin,
    const char *end,
    bool adjustConst) {
  return self->normalizeType(begin, end, adjustConst);
}

//  QtPrivate::QTypeNormalizer::~QTypeNormalizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QTypeNormalizerD1Ev(
    QtPrivate::QTypeNormalizer *self) {
  delete self;
}

//  static bool QtPrivate::QTypeNormalizer::skipToken(const char *&x, const
//      char *e, const char *token, bool msvcKw)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate15QTypeNormalizer9skipTokenERPKcS2_S2_b(
    const char **x,
    const char *e,
    const char *token,
    bool msvcKw) {
  return QtPrivate::QTypeNormalizer::skipToken(*x, e, token, msvcKw);
}

//  void QtPrivate::QTypeNormalizer::normalizeIntegerTypes(const char
//      *&begin, const char *end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QTypeNormalizer21normalizeIntegerTypesERPKcS2_(
    QtPrivate::QTypeNormalizer *self,
    const char **begin,
    const char *end) {
  self->normalizeIntegerTypes(*begin, end);
}

//  void QtPrivate::QTypeNormalizer::skipStructClassOrEnum(const char
//      *&begin, const char *end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QTypeNormalizer21skipStructClassOrEnumERPKcS2_(
    QtPrivate::QTypeNormalizer *self,
    const char **begin,
    const char *end) {
  self->skipStructClassOrEnum(*begin, end);
}

//  void QtPrivate::QTypeNormalizer::skipQtNamespace(const char *&begin,
//      const char *end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QTypeNormalizer15skipQtNamespaceERPKcS2_(
    QtPrivate::QTypeNormalizer *self,
    const char **begin,
    const char *end) {
  self->skipQtNamespace(*begin, end);
}
