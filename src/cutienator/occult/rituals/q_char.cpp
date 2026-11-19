//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qchar.h, Qt 6.12.0. Changes made here are lost.
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

//  UnicodeVersion QChar::currentUnicodeVersion()
extern "C" Q_DECL_EXPORT
QChar::UnicodeVersion ritual_ZN5QChar21currentUnicodeVersionEv() {
  return QChar::currentUnicodeVersion();
}

//  QChar::~QChar()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QCharD1Ev(QChar *self) {
  delete self;
}
