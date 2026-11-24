//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qfontinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qfontinfo.h>
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>
#include <QtGui/qfontvariableaxis.h>
#include <QtCore/qlist.h>

//  QFontInfo::QFontInfo(const QFont &a0)
extern "C" Q_DECL_EXPORT
QFontInfo *ritual_ZN9QFontInfoC1ERK5QFont(const QFont *a0) {
  return new QFontInfo(*a0);
}

//  QFontInfo::QFontInfo(const QFontInfo &a0)
extern "C" Q_DECL_EXPORT
QFontInfo *ritual_ZN9QFontInfoC1ERKS_(const QFontInfo *a0) {
  return new QFontInfo(*a0);
}

//  QFontInfo::~QFontInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QFontInfoD1Ev(QFontInfo *self) {
  delete self;
}

//  QString QFontInfo::family() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFontInfo6familyEv(const QFontInfo *self) {
  return new QString(self->family());
}

//  QString QFontInfo::styleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFontInfo9styleNameEv(const QFontInfo *self) {
  return new QString(self->styleName());
}

//  int QFontInfo::pixelSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QFontInfo9pixelSizeEv(const QFontInfo *self) {
  return self->pixelSize();
}

//  int QFontInfo::pointSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QFontInfo9pointSizeEv(const QFontInfo *self) {
  return self->pointSize();
}

//  qreal QFontInfo::pointSizeF() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QFontInfo10pointSizeFEv(const QFontInfo *self) {
  return self->pointSizeF();
}

//  bool QFontInfo::italic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFontInfo6italicEv(const QFontInfo *self) {
  return self->italic();
}

//  QFont::Style QFontInfo::style() const
extern "C" Q_DECL_EXPORT
QFont::Style ritual_ZNK9QFontInfo5styleEv(const QFontInfo *self) {
  return self->style();
}

//  int QFontInfo::weight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QFontInfo6weightEv(const QFontInfo *self) {
  return self->weight();
}

//  bool QFontInfo::bold() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFontInfo4boldEv(const QFontInfo *self) {
  return self->bold();
}

//  bool QFontInfo::underline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFontInfo9underlineEv(const QFontInfo *self) {
  return self->underline();
}

//  bool QFontInfo::overline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFontInfo8overlineEv(const QFontInfo *self) {
  return self->overline();
}

//  bool QFontInfo::strikeOut() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFontInfo9strikeOutEv(const QFontInfo *self) {
  return self->strikeOut();
}

//  bool QFontInfo::fixedPitch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFontInfo10fixedPitchEv(const QFontInfo *self) {
  return self->fixedPitch();
}

//  QFont::StyleHint QFontInfo::styleHint() const
extern "C" Q_DECL_EXPORT
QFont::StyleHint ritual_ZNK9QFontInfo9styleHintEv(const QFontInfo *self) {
  return self->styleHint();
}

//  QList<QFontVariableAxis> QFontInfo::variableAxes() const
extern "C" Q_DECL_EXPORT
QList<QFontVariableAxis> *ritual_ZNK9QFontInfo12variableAxesEv(
    const QFontInfo *self) {
  return new QList<QFontVariableAxis>(self->variableAxes());
}

#if QT_DEPRECATED_SINCE(6, 0)
//  int QFontInfo::legacyWeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QFontInfo12legacyWeightEv(const QFontInfo *self) {
  return self->legacyWeight();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  bool QFontInfo::exactMatch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFontInfo10exactMatchEv(const QFontInfo *self) {
  return self->exactMatch();
}
