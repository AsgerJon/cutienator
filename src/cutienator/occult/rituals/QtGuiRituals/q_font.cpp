//  Written by dev_tooling.RitualGenerator from the records of QtGui/qfont.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QFont::QFont()
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN5QFontC1Ev() {
  return new QFont();
}

//  QFont::QFont(const QString &family, int pointSize, int weight, bool
//      italic)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN5QFontC1ERK7QStringiib(
    const QString *family,
    int pointSize,
    int weight,
    bool italic) {
  return new QFont(*family, pointSize, weight, italic);
}

//  QFont::QFont(const QStringList &families, int pointSize, int weight, bool
//      italic)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN5QFontC1ERK5QListI7QStringEiib(
    const QList<QString> *families,
    int pointSize,
    int weight,
    bool italic) {
  return new QFont(*families, pointSize, weight, italic);
}

//  QFont::QFont(const QFont &font, const QPaintDevice *pd)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN5QFontC1ERKS_PK12QPaintDevice(
    const QFont *font,
    const QPaintDevice *pd) {
  return new QFont(*font, pd);
}

//  QFont::QFont(const QFont &font)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN5QFontC1ERKS_(const QFont *font) {
  return new QFont(*font);
}

//  QFont::~QFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFontD1Ev(QFont *self) {
  delete self;
}

//  QString QFont::family() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QFont6familyEv(const QFont *self) {
  return new QString(self->family());
}

//  void QFont::setFamily(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont9setFamilyERK7QString(QFont *self, const QString *a0) {
  self->setFamily(*a0);
}

//  QStringList QFont::families() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK5QFont8familiesEv(const QFont *self) {
  return new QList<QString>(self->families());
}

//  void QFont::setFamilies(const QStringList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont11setFamiliesERK5QListI7QStringE(
    QFont *self,
    const QList<QString> *a0) {
  self->setFamilies(*a0);
}

//  QString QFont::styleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QFont9styleNameEv(const QFont *self) {
  return new QString(self->styleName());
}

//  void QFont::setStyleName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont12setStyleNameERK7QString(
    QFont *self,
    const QString *a0) {
  self->setStyleName(*a0);
}

//  int QFont::pointSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QFont9pointSizeEv(const QFont *self) {
  return self->pointSize();
}

//  void QFont::setPointSize(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont12setPointSizeEi(QFont *self, int a0) {
  self->setPointSize(a0);
}

//  qreal QFont::pointSizeF() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK5QFont10pointSizeFEv(const QFont *self) {
  return self->pointSizeF();
}

//  void QFont::setPointSizeF(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont13setPointSizeFEd(QFont *self, qreal a0) {
  self->setPointSizeF(a0);
}

//  int QFont::pixelSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QFont9pixelSizeEv(const QFont *self) {
  return self->pixelSize();
}

//  void QFont::setPixelSize(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont12setPixelSizeEi(QFont *self, int a0) {
  self->setPixelSize(a0);
}

//  Weight QFont::weight() const
extern "C" Q_DECL_EXPORT
QFont::Weight ritual_ZNK5QFont6weightEv(const QFont *self) {
  return self->weight();
}

//  void QFont::setWeight(Weight weight)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont9setWeightENS_6WeightE(
    QFont *self,
    QFont::Weight weight) {
  self->setWeight(weight);
}

//  bool QFont::bold() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont4boldEv(const QFont *self) {
  return self->bold();
}

//  void QFont::setBold(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont7setBoldEb(QFont *self, bool a0) {
  self->setBold(a0);
}

//  void QFont::setStyle(Style style)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont8setStyleENS_5StyleE(QFont *self, QFont::Style style) {
  self->setStyle(style);
}

//  Style QFont::style() const
extern "C" Q_DECL_EXPORT
QFont::Style ritual_ZNK5QFont5styleEv(const QFont *self) {
  return self->style();
}

//  bool QFont::italic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont6italicEv(const QFont *self) {
  return self->italic();
}

//  void QFont::setItalic(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont9setItalicEb(QFont *self, bool b) {
  self->setItalic(b);
}

//  bool QFont::underline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont9underlineEv(const QFont *self) {
  return self->underline();
}

//  void QFont::setUnderline(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont12setUnderlineEb(QFont *self, bool a0) {
  self->setUnderline(a0);
}

//  bool QFont::overline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont8overlineEv(const QFont *self) {
  return self->overline();
}

//  void QFont::setOverline(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont11setOverlineEb(QFont *self, bool a0) {
  self->setOverline(a0);
}

//  bool QFont::strikeOut() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont9strikeOutEv(const QFont *self) {
  return self->strikeOut();
}

//  void QFont::setStrikeOut(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont12setStrikeOutEb(QFont *self, bool a0) {
  self->setStrikeOut(a0);
}

//  bool QFont::fixedPitch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont10fixedPitchEv(const QFont *self) {
  return self->fixedPitch();
}

//  void QFont::setFixedPitch(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont13setFixedPitchEb(QFont *self, bool a0) {
  self->setFixedPitch(a0);
}

//  bool QFont::kerning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont7kerningEv(const QFont *self) {
  return self->kerning();
}

//  void QFont::setKerning(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont10setKerningEb(QFont *self, bool a0) {
  self->setKerning(a0);
}

//  StyleHint QFont::styleHint() const
extern "C" Q_DECL_EXPORT
QFont::StyleHint ritual_ZNK5QFont9styleHintEv(const QFont *self) {
  return self->styleHint();
}

//  StyleStrategy QFont::styleStrategy() const
extern "C" Q_DECL_EXPORT
QFont::StyleStrategy ritual_ZNK5QFont13styleStrategyEv(const QFont *self) {
  return self->styleStrategy();
}

//  void QFont::setStyleHint(StyleHint a0, StyleStrategy a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont12setStyleHintENS_9StyleHintENS_13StyleStrategyE(
    QFont *self,
    QFont::StyleHint a0,
    QFont::StyleStrategy a1) {
  self->setStyleHint(a0, a1);
}

//  void QFont::setStyleStrategy(StyleStrategy s)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont16setStyleStrategyENS_13StyleStrategyE(
    QFont *self,
    QFont::StyleStrategy s) {
  self->setStyleStrategy(s);
}

//  int QFont::stretch() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QFont7stretchEv(const QFont *self) {
  return self->stretch();
}

//  void QFont::setStretch(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont10setStretchEi(QFont *self, int a0) {
  self->setStretch(a0);
}

//  qreal QFont::letterSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK5QFont13letterSpacingEv(const QFont *self) {
  return self->letterSpacing();
}

//  SpacingType QFont::letterSpacingType() const
extern "C" Q_DECL_EXPORT
QFont::SpacingType ritual_ZNK5QFont17letterSpacingTypeEv(const QFont *self) {
  return self->letterSpacingType();
}

//  void QFont::setLetterSpacing(SpacingType type, qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont16setLetterSpacingENS_11SpacingTypeEd(
    QFont *self,
    QFont::SpacingType type,
    qreal spacing) {
  self->setLetterSpacing(type, spacing);
}

//  qreal QFont::wordSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK5QFont11wordSpacingEv(const QFont *self) {
  return self->wordSpacing();
}

//  void QFont::setWordSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont14setWordSpacingEd(QFont *self, qreal spacing) {
  self->setWordSpacing(spacing);
}

//  void QFont::setCapitalization(Capitalization a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont17setCapitalizationENS_14CapitalizationE(
    QFont *self,
    QFont::Capitalization a0) {
  self->setCapitalization(a0);
}

//  Capitalization QFont::capitalization() const
extern "C" Q_DECL_EXPORT
QFont::Capitalization ritual_ZNK5QFont14capitalizationEv(const QFont *self) {
  return self->capitalization();
}

//  void QFont::setHintingPreference(HintingPreference hintingPreference)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont20setHintingPreferenceENS_17HintingPreferenceE(
    QFont *self,
    QFont::HintingPreference hintingPreference) {
  self->setHintingPreference(hintingPreference);
}

//  HintingPreference QFont::hintingPreference() const
extern "C" Q_DECL_EXPORT
QFont::HintingPreference ritual_ZNK5QFont17hintingPreferenceEv(
    const QFont *self) {
  return self->hintingPreference();
}

//  void QFont::setFeature(Tag tag, quint32 value)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont10setFeatureENS_3TagEj(
    QFont *self,
    const QFont::Tag *tag,
    quint32 value) {
  self->setFeature(*tag, value);
}

//  void QFont::unsetFeature(Tag tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont12unsetFeatureENS_3TagE(
    QFont *self,
    const QFont::Tag *tag) {
  self->unsetFeature(*tag);
}

//  quint32 QFont::featureValue(Tag tag) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5QFont12featureValueENS_3TagE(
    const QFont *self,
    const QFont::Tag *tag) {
  return self->featureValue(*tag);
}

//  bool QFont::isFeatureSet(Tag tag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont12isFeatureSetENS_3TagE(
    const QFont *self,
    const QFont::Tag *tag) {
  return self->isFeatureSet(*tag);
}

//  void QFont::clearFeatures()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont13clearFeaturesEv(QFont *self) {
  self->clearFeatures();
}

//  void QFont::setVariableAxis(Tag tag, float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont15setVariableAxisENS_3TagEf(
    QFont *self,
    const QFont::Tag *tag,
    float value) {
  self->setVariableAxis(*tag, value);
}

//  void QFont::unsetVariableAxis(Tag tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont17unsetVariableAxisENS_3TagE(
    QFont *self,
    const QFont::Tag *tag) {
  self->unsetVariableAxis(*tag);
}

//  bool QFont::isVariableAxisSet(Tag tag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont17isVariableAxisSetENS_3TagE(
    const QFont *self,
    const QFont::Tag *tag) {
  return self->isVariableAxisSet(*tag);
}

//  float QFont::variableAxisValue(Tag tag) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK5QFont17variableAxisValueENS_3TagE(
    const QFont *self,
    const QFont::Tag *tag) {
  return self->variableAxisValue(*tag);
}

//  void QFont::clearVariableAxes()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont17clearVariableAxesEv(QFont *self) {
  self->clearVariableAxes();
}

//  bool QFont::exactMatch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont10exactMatchEv(const QFont *self) {
  return self->exactMatch();
}

//  bool QFont::operator==(const QFont &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFonteqERKS_(const QFont *self, const QFont *a0) {
  return self->operator==(*a0);
}

//  bool QFont::operator!=(const QFont &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFontneERKS_(const QFont *self, const QFont *a0) {
  return self->operator!=(*a0);
}

//  bool QFont::operator<(const QFont &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFontltERKS_(const QFont *self, const QFont *a0) {
  return self->operator<(*a0);
}

//  QVariant QFont::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK5QFontcv8QVariantEv(const QFont *self) {
  return new QVariant(self->operator QVariant());
}

//  bool QFont::isCopyOf(const QFont &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont8isCopyOfERKS_(const QFont *self, const QFont *a0) {
  return self->isCopyOf(*a0);
}

//  QString QFont::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QFont3keyEv(const QFont *self) {
  return new QString(self->key());
}

//  QString QFont::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QFont8toStringEv(const QFont *self) {
  return new QString(self->toString());
}

//  bool QFont::fromString(const QString &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFont10fromStringERK7QString(QFont *self, const QString *a0) {
  return self->fromString(*a0);
}

//  QString QFont::substitute(const QString &a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFont10substituteERK7QString(const QString *a0) {
  return new QString(QFont::substitute(*a0));
}

//  QStringList QFont::substitutes(const QString &a0)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN5QFont11substitutesERK7QString(const QString *a0) {
  return new QList<QString>(QFont::substitutes(*a0));
}

//  QStringList QFont::substitutions()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN5QFont13substitutionsEv() {
  return new QList<QString>(QFont::substitutions());
}

//  void QFont::insertSubstitution(const QString &a0, const QString &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont18insertSubstitutionERK7QStringS2_(
    const QString *a0,
    const QString *a1) {
  QFont::insertSubstitution(*a0, *a1);
}

//  void QFont::insertSubstitutions(const QString &a0, const QStringList &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont19insertSubstitutionsERK7QStringRK5QListIS0_E(
    const QString *a0,
    const QList<QString> *a1) {
  QFont::insertSubstitutions(*a0, *a1);
}

//  void QFont::removeSubstitutions(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont19removeSubstitutionsERK7QString(const QString *a0) {
  QFont::removeSubstitutions(*a0);
}

//  void QFont::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont10initializeEv() {
  QFont::initialize();
}

//  void QFont::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont7cleanupEv() {
  QFont::cleanup();
}

//  void QFont::cacheStatistics()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont15cacheStatisticsEv() {
  QFont::cacheStatistics();
}

//  QString QFont::defaultFamily() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QFont13defaultFamilyEv(const QFont *self) {
  return new QString(self->defaultFamily());
}

//  QFont QFont::resolve(const QFont &a0) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK5QFont7resolveERKS_(const QFont *self, const QFont *a0) {
  return new QFont(self->resolve(*a0));
}

//  uint QFont::resolveMask() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK5QFont11resolveMaskEv(const QFont *self) {
  return self->resolveMask();
}

//  void QFont::setResolveMask(uint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont14setResolveMaskEj(QFont *self, uint mask) {
  self->setResolveMask(mask);
}

//  void QFont::setLegacyWeight(int legacyWeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont15setLegacyWeightEi(QFont *self, int legacyWeight) {
  self->setLegacyWeight(legacyWeight);
}

//  int QFont::legacyWeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QFont12legacyWeightEv(const QFont *self) {
  return self->legacyWeight();
}

//  QDebug operator<<(QDebug a0, const QFont &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK5QFont(const QDebug *a0, const QFont *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
