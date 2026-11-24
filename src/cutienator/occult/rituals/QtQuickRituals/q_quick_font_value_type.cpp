//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qvariant.h>
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  void QQuickFontValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType20qt_qmlMarker_foreignEv(
    QQuickFontValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQuickFontValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType21qt_qmlMarker_extendedEv(
    QQuickFontValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QVariant QQuickFontValueType::create(const QJSValue &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN19QQuickFontValueType6createERK8QJSValue(
    const QJSValue *value) {
  return new QVariant(QQuickFontValueType::create(*value));
}

//  QQuickFontValueType::QQuickFontValueType()
extern "C" Q_DECL_EXPORT
QQuickFontValueType *ritual_ZN19QQuickFontValueTypeC1Ev() {
  return new QQuickFontValueType();
}

//  QQuickFontValueType::QQuickFontValueType(const QFont &font)
extern "C" Q_DECL_EXPORT
QQuickFontValueType *ritual_ZN19QQuickFontValueTypeC1ERK5QFont(
    const QFont *font) {
  return new QQuickFontValueType(*font);
}

//  QString QQuickFontValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickFontValueType8toStringEv(
    const QQuickFontValueType *self) {
  return new QString(self->toString());
}

//  QString QQuickFontValueType::family() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickFontValueType6familyEv(
    const QQuickFontValueType *self) {
  return new QString(self->family());
}

//  void QQuickFontValueType::setFamily(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType9setFamilyERK7QString(
    QQuickFontValueType *self,
    const QString *a0) {
  self->setFamily(*a0);
}

//  QString QQuickFontValueType::styleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickFontValueType9styleNameEv(
    const QQuickFontValueType *self) {
  return new QString(self->styleName());
}

//  void QQuickFontValueType::setStyleName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType12setStyleNameERK7QString(
    QQuickFontValueType *self,
    const QString *a0) {
  self->setStyleName(*a0);
}

//  bool QQuickFontValueType::bold() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickFontValueType4boldEv(
    const QQuickFontValueType *self) {
  return self->bold();
}

//  void QQuickFontValueType::setBold(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType7setBoldEb(
    QQuickFontValueType *self,
    bool b) {
  self->setBold(b);
}

//  int QQuickFontValueType::weight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickFontValueType6weightEv(
    const QQuickFontValueType *self) {
  return self->weight();
}

//  void QQuickFontValueType::setWeight(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType9setWeightEi(
    QQuickFontValueType *self,
    int a0) {
  self->setWeight(a0);
}

//  bool QQuickFontValueType::italic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickFontValueType6italicEv(
    const QQuickFontValueType *self) {
  return self->italic();
}

//  void QQuickFontValueType::setItalic(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType9setItalicEb(
    QQuickFontValueType *self,
    bool b) {
  self->setItalic(b);
}

//  bool QQuickFontValueType::underline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickFontValueType9underlineEv(
    const QQuickFontValueType *self) {
  return self->underline();
}

//  void QQuickFontValueType::setUnderline(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType12setUnderlineEb(
    QQuickFontValueType *self,
    bool b) {
  self->setUnderline(b);
}

//  bool QQuickFontValueType::overline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickFontValueType8overlineEv(
    const QQuickFontValueType *self) {
  return self->overline();
}

//  void QQuickFontValueType::setOverline(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType11setOverlineEb(
    QQuickFontValueType *self,
    bool b) {
  self->setOverline(b);
}

//  bool QQuickFontValueType::strikeout() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickFontValueType9strikeoutEv(
    const QQuickFontValueType *self) {
  return self->strikeout();
}

//  void QQuickFontValueType::setStrikeout(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType12setStrikeoutEb(
    QQuickFontValueType *self,
    bool b) {
  self->setStrikeout(b);
}

//  qreal QQuickFontValueType::pointSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickFontValueType9pointSizeEv(
    const QQuickFontValueType *self) {
  return self->pointSize();
}

//  void QQuickFontValueType::setPointSize(qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType12setPointSizeEd(
    QQuickFontValueType *self,
    qreal size) {
  self->setPointSize(size);
}

//  int QQuickFontValueType::pixelSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickFontValueType9pixelSizeEv(
    const QQuickFontValueType *self) {
  return self->pixelSize();
}

//  void QQuickFontValueType::setPixelSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType12setPixelSizeEi(
    QQuickFontValueType *self,
    int size) {
  self->setPixelSize(size);
}

//  QQuickFontEnums::Capitalization QQuickFontValueType::capitalization()
//      const
extern "C" Q_DECL_EXPORT
QQuickFontEnums::Capitalization ritual_ZNK19QQuickFontValueType14capitalizationEv(
    const QQuickFontValueType *self) {
  return self->capitalization();
}

//  void
//      QQuickFontValueType::setCapitalization(QQuickFontEnums::Capitalizatio
//      n a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType17setCapitalizationEN15QQuickFontEnums14CapitalizationE(
    QQuickFontValueType *self,
    QQuickFontEnums::Capitalization a0) {
  self->setCapitalization(a0);
}

//  qreal QQuickFontValueType::letterSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickFontValueType13letterSpacingEv(
    const QQuickFontValueType *self) {
  return self->letterSpacing();
}

//  void QQuickFontValueType::setLetterSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType16setLetterSpacingEd(
    QQuickFontValueType *self,
    qreal spacing) {
  self->setLetterSpacing(spacing);
}

//  qreal QQuickFontValueType::wordSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickFontValueType11wordSpacingEv(
    const QQuickFontValueType *self) {
  return self->wordSpacing();
}

//  void QQuickFontValueType::setWordSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType14setWordSpacingEd(
    QQuickFontValueType *self,
    qreal spacing) {
  self->setWordSpacing(spacing);
}

//  QQuickFontEnums::HintingPreference
//      QQuickFontValueType::hintingPreference() const
extern "C" Q_DECL_EXPORT
QQuickFontEnums::HintingPreference ritual_ZNK19QQuickFontValueType17hintingPreferenceEv(
    const QQuickFontValueType *self) {
  return self->hintingPreference();
}

//  void QQuickFontValueType::setHintingPreference(QQuickFontEnums::HintingPr
//      eference a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType20setHintingPreferenceEN15QQuickFontEnums17HintingPreferenceE(
    QQuickFontValueType *self,
    QQuickFontEnums::HintingPreference a0) {
  self->setHintingPreference(a0);
}

//  bool QQuickFontValueType::kerning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickFontValueType7kerningEv(
    const QQuickFontValueType *self) {
  return self->kerning();
}

//  void QQuickFontValueType::setKerning(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType10setKerningEb(
    QQuickFontValueType *self,
    bool b) {
  self->setKerning(b);
}

//  bool QQuickFontValueType::preferShaping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickFontValueType13preferShapingEv(
    const QQuickFontValueType *self) {
  return self->preferShaping();
}

//  void QQuickFontValueType::setPreferShaping(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType16setPreferShapingEb(
    QQuickFontValueType *self,
    bool b) {
  self->setPreferShaping(b);
}

//  QVariantMap QQuickFontValueType::features() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK19QQuickFontValueType8featuresEv(
    const QQuickFontValueType *self) {
  return new QMap<QString, QVariant>(self->features());
}

//  void QQuickFontValueType::setFeatures(const QVariantMap &features)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType11setFeaturesERK4QMapI7QString8QVariantE(
    QQuickFontValueType *self,
    const QMap<QString, QVariant> *features) {
  self->setFeatures(*features);
}

//  QVariantMap QQuickFontValueType::variableAxes() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK19QQuickFontValueType12variableAxesEv(
    const QQuickFontValueType *self) {
  return new QMap<QString, QVariant>(self->variableAxes());
}

//  void QQuickFontValueType::setVariableAxes(const QVariantMap
//      &variableAxes)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType15setVariableAxesERK4QMapI7QString8QVariantE(
    QQuickFontValueType *self,
    const QMap<QString, QVariant> *variableAxes) {
  self->setVariableAxes(*variableAxes);
}

//  bool QQuickFontValueType::contextFontMerging() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickFontValueType18contextFontMergingEv(
    const QQuickFontValueType *self) {
  return self->contextFontMerging();
}

//  void QQuickFontValueType::setContextFontMerging(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType21setContextFontMergingEb(
    QQuickFontValueType *self,
    bool b) {
  self->setContextFontMerging(b);
}

//  bool QQuickFontValueType::preferTypoLineMetrics() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickFontValueType21preferTypoLineMetricsEv(
    const QQuickFontValueType *self) {
  return self->preferTypoLineMetrics();
}

//  void QQuickFontValueType::setPreferTypoLineMetrics(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueType24setPreferTypoLineMetricsEb(
    QQuickFontValueType *self,
    bool b) {
  self->setPreferTypoLineMetrics(b);
}

//  QQuickFontValueType::~QQuickFontValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickFontValueTypeD1Ev(QQuickFontValueType *self) {
  delete self;
}
