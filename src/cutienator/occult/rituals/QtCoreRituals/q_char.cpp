//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qchar.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by hand,
//  instances of templates of the class: 4. Kept as it is when the generator
//  runs again. Also added by hand on 2026-11-25, rituals for functions the
//  generator leaves out: 1.
#include <QtCore/qchar.h>
#include <QtCore/qstring.h>

//  QChar::QChar()
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN5QCharC1Ev() {
  return new QChar();
}

//  QChar::QChar(uchar c, uchar r)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN5QCharC1Ehh(uchar c, uchar r) {
  return new QChar(c, r);
}

//  QChar QChar::fromUcs2(char16_t c)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN5QChar8fromUcs2EDs(char16_t c) {
  return new QChar(QChar::fromUcs2(c));
}

//  Category QChar::category() const
extern "C" Q_DECL_EXPORT
QChar::Category ritual_ZNK5QChar8categoryEv(const QChar *self) {
  return self->category();
}

//  Direction QChar::direction() const
extern "C" Q_DECL_EXPORT
QChar::Direction ritual_ZNK5QChar9directionEv(const QChar *self) {
  return self->direction();
}

//  JoiningType QChar::joiningType() const
extern "C" Q_DECL_EXPORT
QChar::JoiningType ritual_ZNK5QChar11joiningTypeEv(const QChar *self) {
  return self->joiningType();
}

//  unsigned char QChar::combiningClass() const
extern "C" Q_DECL_EXPORT
unsigned char ritual_ZNK5QChar14combiningClassEv(const QChar *self) {
  return self->combiningClass();
}

//  QChar QChar::mirroredChar() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK5QChar12mirroredCharEv(const QChar *self) {
  return new QChar(self->mirroredChar());
}

//  bool QChar::hasMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar11hasMirroredEv(const QChar *self) {
  return self->hasMirrored();
}

//  QString QChar::decomposition() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QChar13decompositionEv(const QChar *self) {
  return new QString(self->decomposition());
}

//  Decomposition QChar::decompositionTag() const
extern "C" Q_DECL_EXPORT
QChar::Decomposition ritual_ZNK5QChar16decompositionTagEv(
    const QChar *self) {
  return self->decompositionTag();
}

//  int QChar::digitValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QChar10digitValueEv(const QChar *self) {
  return self->digitValue();
}

//  QChar QChar::toLower() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK5QChar7toLowerEv(const QChar *self) {
  return new QChar(self->toLower());
}

//  QChar QChar::toUpper() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK5QChar7toUpperEv(const QChar *self) {
  return new QChar(self->toUpper());
}

//  QChar QChar::toTitleCase() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK5QChar11toTitleCaseEv(const QChar *self) {
  return new QChar(self->toTitleCase());
}

//  QChar QChar::toCaseFolded() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK5QChar12toCaseFoldedEv(const QChar *self) {
  return new QChar(self->toCaseFolded());
}

//  Script QChar::script() const
extern "C" Q_DECL_EXPORT
QChar::Script ritual_ZNK5QChar6scriptEv(const QChar *self) {
  return self->script();
}

//  UnicodeVersion QChar::unicodeVersion() const
extern "C" Q_DECL_EXPORT
QChar::UnicodeVersion ritual_ZNK5QChar14unicodeVersionEv(const QChar *self) {
  return self->unicodeVersion();
}

//  char QChar::toLatin1() const
extern "C" Q_DECL_EXPORT
char ritual_ZNK5QChar8toLatin1Ev(const QChar *self) {
  return self->toLatin1();
}

//  char16_t QChar::unicode() const
extern "C" Q_DECL_EXPORT
char16_t ritual_ZNK5QChar7unicodeEv(const QChar *self) {
  return self->unicode();
}

//  QChar QChar::fromLatin1(char c)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN5QChar10fromLatin1Ec(char c) {
  return new QChar(QChar::fromLatin1(c));
}

//  bool QChar::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar6isNullEv(const QChar *self) {
  return self->isNull();
}

//  bool QChar::isPrint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar7isPrintEv(const QChar *self) {
  return self->isPrint();
}

//  bool QChar::isSpace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar7isSpaceEv(const QChar *self) {
  return self->isSpace();
}

//  bool QChar::isMark() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar6isMarkEv(const QChar *self) {
  return self->isMark();
}

//  bool QChar::isPunct() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar7isPunctEv(const QChar *self) {
  return self->isPunct();
}

//  bool QChar::isSymbol() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar8isSymbolEv(const QChar *self) {
  return self->isSymbol();
}

//  bool QChar::isLetter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar8isLetterEv(const QChar *self) {
  return self->isLetter();
}

//  bool QChar::isNumber() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar8isNumberEv(const QChar *self) {
  return self->isNumber();
}

//  bool QChar::isLetterOrNumber() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar16isLetterOrNumberEv(const QChar *self) {
  return self->isLetterOrNumber();
}

//  bool QChar::isDigit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar7isDigitEv(const QChar *self) {
  return self->isDigit();
}

//  bool QChar::isLower() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar7isLowerEv(const QChar *self) {
  return self->isLower();
}

//  bool QChar::isUpper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar7isUpperEv(const QChar *self) {
  return self->isUpper();
}

//  bool QChar::isTitleCase() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar11isTitleCaseEv(const QChar *self) {
  return self->isTitleCase();
}

//  bool QChar::isNonCharacter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar14isNonCharacterEv(const QChar *self) {
  return self->isNonCharacter();
}

//  bool QChar::isHighSurrogate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar15isHighSurrogateEv(const QChar *self) {
  return self->isHighSurrogate();
}

//  bool QChar::isLowSurrogate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar14isLowSurrogateEv(const QChar *self) {
  return self->isLowSurrogate();
}

//  bool QChar::isSurrogate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QChar11isSurrogateEv(const QChar *self) {
  return self->isSurrogate();
}

//  uchar QChar::cell() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK5QChar4cellEv(const QChar *self) {
  return self->cell();
}

//  uchar QChar::row() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK5QChar3rowEv(const QChar *self) {
  return self->row();
}

//  void QChar::setCell(uchar acell)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QChar7setCellEh(QChar *self, uchar acell) {
  self->setCell(acell);
}

//  void QChar::setRow(uchar arow)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QChar6setRowEh(QChar *self, uchar arow) {
  self->setRow(arow);
}

//  bool QChar::isNonCharacter(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar14isNonCharacterEDi(char32_t ucs4) {
  return QChar::isNonCharacter(ucs4);
}

//  bool QChar::isHighSurrogate(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar15isHighSurrogateEDi(char32_t ucs4) {
  return QChar::isHighSurrogate(ucs4);
}

//  bool QChar::isLowSurrogate(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar14isLowSurrogateEDi(char32_t ucs4) {
  return QChar::isLowSurrogate(ucs4);
}

//  bool QChar::isSurrogate(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar11isSurrogateEDi(char32_t ucs4) {
  return QChar::isSurrogate(ucs4);
}

//  bool QChar::requiresSurrogates(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar18requiresSurrogatesEDi(char32_t ucs4) {
  return QChar::requiresSurrogates(ucs4);
}

//  char32_t QChar::surrogateToUcs4(char16_t high, char16_t low)
extern "C" Q_DECL_EXPORT
char32_t ritual_ZN5QChar15surrogateToUcs4EDsDs(char16_t high, char16_t low) {
  return QChar::surrogateToUcs4(high, low);
}

//  char32_t QChar::surrogateToUcs4(QChar high, QChar low)
extern "C" Q_DECL_EXPORT
char32_t ritual_ZN5QChar15surrogateToUcs4ES_S_(
    const QChar *high,
    const QChar *low) {
  return QChar::surrogateToUcs4(*high, *low);
}

//  char16_t QChar::highSurrogate(char32_t ucs4)
extern "C" Q_DECL_EXPORT
char16_t ritual_ZN5QChar13highSurrogateEDi(char32_t ucs4) {
  return QChar::highSurrogate(ucs4);
}

//  char16_t QChar::lowSurrogate(char32_t ucs4)
extern "C" Q_DECL_EXPORT
char16_t ritual_ZN5QChar12lowSurrogateEDi(char32_t ucs4) {
  return QChar::lowSurrogate(ucs4);
}

//  Category QChar::category(char32_t ucs4)
extern "C" Q_DECL_EXPORT
QChar::Category ritual_ZN5QChar8categoryEDi(char32_t ucs4) {
  return QChar::category(ucs4);
}

//  Direction QChar::direction(char32_t ucs4)
extern "C" Q_DECL_EXPORT
QChar::Direction ritual_ZN5QChar9directionEDi(char32_t ucs4) {
  return QChar::direction(ucs4);
}

//  JoiningType QChar::joiningType(char32_t ucs4)
extern "C" Q_DECL_EXPORT
QChar::JoiningType ritual_ZN5QChar11joiningTypeEDi(char32_t ucs4) {
  return QChar::joiningType(ucs4);
}

//  unsigned char QChar::combiningClass(char32_t ucs4)
extern "C" Q_DECL_EXPORT
unsigned char ritual_ZN5QChar14combiningClassEDi(char32_t ucs4) {
  return QChar::combiningClass(ucs4);
}

//  char32_t QChar::mirroredChar(char32_t ucs4)
extern "C" Q_DECL_EXPORT
char32_t ritual_ZN5QChar12mirroredCharEDi(char32_t ucs4) {
  return QChar::mirroredChar(ucs4);
}

//  bool QChar::hasMirrored(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar11hasMirroredEDi(char32_t ucs4) {
  return QChar::hasMirrored(ucs4);
}

//  QString QChar::decomposition(char32_t ucs4)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QChar13decompositionEDi(char32_t ucs4) {
  return new QString(QChar::decomposition(ucs4));
}

//  Decomposition QChar::decompositionTag(char32_t ucs4)
extern "C" Q_DECL_EXPORT
QChar::Decomposition ritual_ZN5QChar16decompositionTagEDi(char32_t ucs4) {
  return QChar::decompositionTag(ucs4);
}

//  int QChar::digitValue(char32_t ucs4)
extern "C" Q_DECL_EXPORT
int ritual_ZN5QChar10digitValueEDi(char32_t ucs4) {
  return QChar::digitValue(ucs4);
}

//  char32_t QChar::toLower(char32_t ucs4)
extern "C" Q_DECL_EXPORT
char32_t ritual_ZN5QChar7toLowerEDi(char32_t ucs4) {
  return QChar::toLower(ucs4);
}

//  char32_t QChar::toUpper(char32_t ucs4)
extern "C" Q_DECL_EXPORT
char32_t ritual_ZN5QChar7toUpperEDi(char32_t ucs4) {
  return QChar::toUpper(ucs4);
}

//  char32_t QChar::toTitleCase(char32_t ucs4)
extern "C" Q_DECL_EXPORT
char32_t ritual_ZN5QChar11toTitleCaseEDi(char32_t ucs4) {
  return QChar::toTitleCase(ucs4);
}

//  char32_t QChar::toCaseFolded(char32_t ucs4)
extern "C" Q_DECL_EXPORT
char32_t ritual_ZN5QChar12toCaseFoldedEDi(char32_t ucs4) {
  return QChar::toCaseFolded(ucs4);
}

//  Script QChar::script(char32_t ucs4)
extern "C" Q_DECL_EXPORT
QChar::Script ritual_ZN5QChar6scriptEDi(char32_t ucs4) {
  return QChar::script(ucs4);
}

//  UnicodeVersion QChar::unicodeVersion(char32_t ucs4)
extern "C" Q_DECL_EXPORT
QChar::UnicodeVersion ritual_ZN5QChar14unicodeVersionEDi(char32_t ucs4) {
  return QChar::unicodeVersion(ucs4);
}

//  UnicodeVersion QChar::currentUnicodeVersion()
extern "C" Q_DECL_EXPORT
QChar::UnicodeVersion ritual_ZN5QChar21currentUnicodeVersionEv() {
  return QChar::currentUnicodeVersion();
}

//  bool QChar::isPrint(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar7isPrintEDi(char32_t ucs4) {
  return QChar::isPrint(ucs4);
}

//  bool QChar::isSpace(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar7isSpaceEDi(char32_t ucs4) {
  return QChar::isSpace(ucs4);
}

//  bool QChar::isMark(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar6isMarkEDi(char32_t ucs4) {
  return QChar::isMark(ucs4);
}

//  bool QChar::isPunct(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar7isPunctEDi(char32_t ucs4) {
  return QChar::isPunct(ucs4);
}

//  bool QChar::isSymbol(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar8isSymbolEDi(char32_t ucs4) {
  return QChar::isSymbol(ucs4);
}

//  bool QChar::isLetter(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar8isLetterEDi(char32_t ucs4) {
  return QChar::isLetter(ucs4);
}

//  bool QChar::isNumber(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar8isNumberEDi(char32_t ucs4) {
  return QChar::isNumber(ucs4);
}

//  bool QChar::isLetterOrNumber(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar16isLetterOrNumberEDi(char32_t ucs4) {
  return QChar::isLetterOrNumber(ucs4);
}

//  bool QChar::isDigit(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar7isDigitEDi(char32_t ucs4) {
  return QChar::isDigit(ucs4);
}

//  bool QChar::isLower(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar7isLowerEDi(char32_t ucs4) {
  return QChar::isLower(ucs4);
}

//  bool QChar::isUpper(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar7isUpperEDi(char32_t ucs4) {
  return QChar::isUpper(ucs4);
}

//  bool QChar::isTitleCase(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar11isTitleCaseEDi(char32_t ucs4) {
  return QChar::isTitleCase(ucs4);
}

//  bool operator==(const QChar &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QCharS1_(const QChar *lhs, const QChar *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QChar &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QCharS1_(const QChar *lhs, const QChar *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QChar &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK5QCharS1_(const QChar *lhs, const QChar *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QChar &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK5QCharS1_(const QChar *lhs, const QChar *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QChar &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK5QCharS1_(const QChar *lhs, const QChar *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QChar &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK5QCharS1_(const QChar *lhs, const QChar *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QChar &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QCharRKDn(const QChar *lhs) {
  return operator==(*lhs, nullptr);
}

//  bool operator!=(const QChar &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QCharRKDn(const QChar *lhs) {
  return operator!=(*lhs, nullptr);
}

//  bool operator<(const QChar &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK5QCharRKDn(const QChar *lhs) {
  return operator<(*lhs, nullptr);
}

//  bool operator>(const QChar &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK5QCharRKDn(const QChar *lhs) {
  return operator>(*lhs, nullptr);
}

//  bool operator<=(const QChar &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK5QCharRKDn(const QChar *lhs) {
  return operator<=(*lhs, nullptr);
}

//  bool operator>=(const QChar &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK5QCharRKDn(const QChar *lhs) {
  return operator>=(*lhs, nullptr);
}

//  bool operator==(const std::nullptr_t &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKDnRK5QChar(const QChar *rhs) {
  return operator==(nullptr, *rhs);
}

//  bool operator!=(const std::nullptr_t &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKDnRK5QChar(const QChar *rhs) {
  return operator!=(nullptr, *rhs);
}

//  bool operator<(const std::nullptr_t &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKDnRK5QChar(const QChar *rhs) {
  return operator<(nullptr, *rhs);
}

//  bool operator>(const std::nullptr_t &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKDnRK5QChar(const QChar *rhs) {
  return operator>(nullptr, *rhs);
}

//  bool operator<=(const std::nullptr_t &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKDnRK5QChar(const QChar *rhs) {
  return operator<=(nullptr, *rhs);
}

//  bool operator>=(const std::nullptr_t &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKDnRK5QChar(const QChar *rhs) {
  return operator>=(nullptr, *rhs);
}

//  bool QChar::isSpace_helper(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar14isSpace_helperEDi(char32_t ucs4) {
  return QChar::isSpace_helper(ucs4);
}

//  bool QChar::isLetter_helper(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar15isLetter_helperEDi(char32_t ucs4) {
  return QChar::isLetter_helper(ucs4);
}

//  bool QChar::isNumber_helper(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar15isNumber_helperEDi(char32_t ucs4) {
  return QChar::isNumber_helper(ucs4);
}

//  bool QChar::isLetterOrNumber_helper(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar23isLetterOrNumber_helperEDi(char32_t ucs4) {
  return QChar::isLetterOrNumber_helper(ucs4);
}

//  bool QChar::equal_helper(QChar lhs, const char *rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QChar12equal_helperES_PKc(const QChar *lhs, const char *rhs) {
  return QChar::equal_helper(*lhs, rhs);
}

//  int QChar::compare_helper(QChar lhs, const char *rhs)
extern "C" Q_DECL_EXPORT
int ritual_ZN5QChar14compare_helperES_PKc(
    const QChar *lhs,
    const char *rhs) {
  return QChar::compare_helper(*lhs, rhs);
}

//  QChar::~QChar()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QCharD1Ev(QChar *self) {
  delete self;
}

//  template <typename Char, if_implicit_conversion_char<Char> = true>
//  constexpr QChar::QChar<char16_t, true>(const char16_t ch)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN5QCharC1IDsLb1EEET_(char16_t ch) {
  return new QChar(ch);
}

//  template <typename Char, if_explicit_conversion_char<Char> = true>
//  constexpr explicit QChar::QChar<char32_t, true>(const char32_t ch)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN5QCharC1IDiLb1EEET_(char32_t ch) {
  return new QChar(ch);
}

//  template <typename Char, if_explicit_conversion_char<Char> = true>
//  constexpr explicit QChar::QChar<int, true>(const int ch)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN5QCharC1IiLb1EEET_(int ch) {
  return new QChar(ch);
}

#if !defined(QT_NO_CAST_FROM_ASCII)
//  template <typename Char, if_implicit_ascii_warn_char<Char> = true>
//  constexpr QChar::QChar<char, true>(const char ch)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN5QCharC1IcLb1EEET_(char ch) {
  return new QChar(ch);
}
#endif  // !defined(QT_NO_CAST_FROM_ASCII)

//  char16_t &QChar::unicode()
extern "C" Q_DECL_EXPORT
char16_t *ritual_ZN5QChar7unicodeEv(
    QChar *self) {
  return &(self->unicode());
}
