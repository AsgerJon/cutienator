//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextformat.h>
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <QtGui/qpen.h>
#include <QtCore/qlist.h>

//  QTextCharFormat::QTextCharFormat()
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZN15QTextCharFormatC1Ev() {
  return new QTextCharFormat();
}

//  bool QTextCharFormat::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTextCharFormat7isValidEv(const QTextCharFormat *self) {
  return self->isValid();
}

//  void QTextCharFormat::setFont(const QFont &font,
//      FontPropertiesInheritanceBehavior behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat7setFontERK5QFontNS_33FontPropertiesInheritanceBehaviorE(
    QTextCharFormat *self,
    const QFont *font,
    QTextCharFormat::FontPropertiesInheritanceBehavior behavior) {
  self->setFont(*font, behavior);
}

//  QFont QTextCharFormat::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QTextCharFormat4fontEv(const QTextCharFormat *self) {
  return new QFont(self->font());
}

//  void QTextCharFormat::setFontFamily(const QString &family)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat13setFontFamilyERK7QString(
    QTextCharFormat *self,
    const QString *family) {
  self->setFontFamily(*family);
}

//  QString QTextCharFormat::fontFamily() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QTextCharFormat10fontFamilyEv(
    const QTextCharFormat *self) {
  return new QString(self->fontFamily());
}

//  void QTextCharFormat::setFontFamilies(const QStringList &families)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat15setFontFamiliesERK5QListI7QStringE(
    QTextCharFormat *self,
    const QList<QString> *families) {
  self->setFontFamilies(*families);
}

//  QVariant QTextCharFormat::fontFamilies() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QTextCharFormat12fontFamiliesEv(
    const QTextCharFormat *self) {
  return new QVariant(self->fontFamilies());
}

//  void QTextCharFormat::setFontStyleName(const QString &styleName)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat16setFontStyleNameERK7QString(
    QTextCharFormat *self,
    const QString *styleName) {
  self->setFontStyleName(*styleName);
}

//  QVariant QTextCharFormat::fontStyleName() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QTextCharFormat13fontStyleNameEv(
    const QTextCharFormat *self) {
  return new QVariant(self->fontStyleName());
}

//  void QTextCharFormat::setFontPointSize(qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat16setFontPointSizeEd(
    QTextCharFormat *self,
    qreal size) {
  self->setFontPointSize(size);
}

//  qreal QTextCharFormat::fontPointSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QTextCharFormat13fontPointSizeEv(
    const QTextCharFormat *self) {
  return self->fontPointSize();
}

//  void QTextCharFormat::setFontWeight(int weight)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat13setFontWeightEi(
    QTextCharFormat *self,
    int weight) {
  self->setFontWeight(weight);
}

//  int QTextCharFormat::fontWeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextCharFormat10fontWeightEv(const QTextCharFormat *self) {
  return self->fontWeight();
}

//  void QTextCharFormat::setFontItalic(bool italic)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat13setFontItalicEb(
    QTextCharFormat *self,
    bool italic) {
  self->setFontItalic(italic);
}

//  bool QTextCharFormat::fontItalic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTextCharFormat10fontItalicEv(const QTextCharFormat *self) {
  return self->fontItalic();
}

//  void QTextCharFormat::setFontCapitalization(QFont::Capitalization
//      capitalization)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat21setFontCapitalizationEN5QFont14CapitalizationE(
    QTextCharFormat *self,
    QFont::Capitalization capitalization) {
  self->setFontCapitalization(capitalization);
}

//  QFont::Capitalization QTextCharFormat::fontCapitalization() const
extern "C" Q_DECL_EXPORT
QFont::Capitalization ritual_ZNK15QTextCharFormat18fontCapitalizationEv(
    const QTextCharFormat *self) {
  return self->fontCapitalization();
}

//  void QTextCharFormat::setFontLetterSpacingType(QFont::SpacingType
//      letterSpacingType)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat24setFontLetterSpacingTypeEN5QFont11SpacingTypeE(
    QTextCharFormat *self,
    QFont::SpacingType letterSpacingType) {
  self->setFontLetterSpacingType(letterSpacingType);
}

//  QFont::SpacingType QTextCharFormat::fontLetterSpacingType() const
extern "C" Q_DECL_EXPORT
QFont::SpacingType ritual_ZNK15QTextCharFormat21fontLetterSpacingTypeEv(
    const QTextCharFormat *self) {
  return self->fontLetterSpacingType();
}

//  void QTextCharFormat::setFontLetterSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat20setFontLetterSpacingEd(
    QTextCharFormat *self,
    qreal spacing) {
  self->setFontLetterSpacing(spacing);
}

//  qreal QTextCharFormat::fontLetterSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QTextCharFormat17fontLetterSpacingEv(
    const QTextCharFormat *self) {
  return self->fontLetterSpacing();
}

//  void QTextCharFormat::setFontWordSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat18setFontWordSpacingEd(
    QTextCharFormat *self,
    qreal spacing) {
  self->setFontWordSpacing(spacing);
}

//  qreal QTextCharFormat::fontWordSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QTextCharFormat15fontWordSpacingEv(
    const QTextCharFormat *self) {
  return self->fontWordSpacing();
}

//  void QTextCharFormat::setFontUnderline(bool underline)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat16setFontUnderlineEb(
    QTextCharFormat *self,
    bool underline) {
  self->setFontUnderline(underline);
}

//  bool QTextCharFormat::fontUnderline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTextCharFormat13fontUnderlineEv(
    const QTextCharFormat *self) {
  return self->fontUnderline();
}

//  void QTextCharFormat::setFontOverline(bool overline)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat15setFontOverlineEb(
    QTextCharFormat *self,
    bool overline) {
  self->setFontOverline(overline);
}

//  bool QTextCharFormat::fontOverline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTextCharFormat12fontOverlineEv(
    const QTextCharFormat *self) {
  return self->fontOverline();
}

//  void QTextCharFormat::setFontStrikeOut(bool strikeOut)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat16setFontStrikeOutEb(
    QTextCharFormat *self,
    bool strikeOut) {
  self->setFontStrikeOut(strikeOut);
}

//  bool QTextCharFormat::fontStrikeOut() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTextCharFormat13fontStrikeOutEv(
    const QTextCharFormat *self) {
  return self->fontStrikeOut();
}

//  void QTextCharFormat::setUnderlineColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat17setUnderlineColorERK6QColor(
    QTextCharFormat *self,
    const QColor *color) {
  self->setUnderlineColor(*color);
}

//  QColor QTextCharFormat::underlineColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QTextCharFormat14underlineColorEv(
    const QTextCharFormat *self) {
  return new QColor(self->underlineColor());
}

//  void QTextCharFormat::setFontFixedPitch(bool fixedPitch)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat17setFontFixedPitchEb(
    QTextCharFormat *self,
    bool fixedPitch) {
  self->setFontFixedPitch(fixedPitch);
}

//  bool QTextCharFormat::fontFixedPitch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTextCharFormat14fontFixedPitchEv(
    const QTextCharFormat *self) {
  return self->fontFixedPitch();
}

//  void QTextCharFormat::setFontStretch(int factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat14setFontStretchEi(
    QTextCharFormat *self,
    int factor) {
  self->setFontStretch(factor);
}

//  int QTextCharFormat::fontStretch() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextCharFormat11fontStretchEv(const QTextCharFormat *self) {
  return self->fontStretch();
}

//  void QTextCharFormat::setFontStyleHint(QFont::StyleHint hint,
//      QFont::StyleStrategy strategy)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat16setFontStyleHintEN5QFont9StyleHintENS0_13StyleStrategyE(
    QTextCharFormat *self,
    QFont::StyleHint hint,
    QFont::StyleStrategy strategy) {
  self->setFontStyleHint(hint, strategy);
}

//  void QTextCharFormat::setFontStyleStrategy(QFont::StyleStrategy strategy)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat20setFontStyleStrategyEN5QFont13StyleStrategyE(
    QTextCharFormat *self,
    QFont::StyleStrategy strategy) {
  self->setFontStyleStrategy(strategy);
}

//  QFont::StyleHint QTextCharFormat::fontStyleHint() const
extern "C" Q_DECL_EXPORT
QFont::StyleHint ritual_ZNK15QTextCharFormat13fontStyleHintEv(
    const QTextCharFormat *self) {
  return self->fontStyleHint();
}

//  QFont::StyleStrategy QTextCharFormat::fontStyleStrategy() const
extern "C" Q_DECL_EXPORT
QFont::StyleStrategy ritual_ZNK15QTextCharFormat17fontStyleStrategyEv(
    const QTextCharFormat *self) {
  return self->fontStyleStrategy();
}

//  void QTextCharFormat::setFontHintingPreference(QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat24setFontHintingPreferenceEN5QFont17HintingPreferenceE(
    QTextCharFormat *self,
    QFont::HintingPreference hintingPreference) {
  self->setFontHintingPreference(hintingPreference);
}

//  QFont::HintingPreference QTextCharFormat::fontHintingPreference() const
extern "C" Q_DECL_EXPORT
QFont::HintingPreference ritual_ZNK15QTextCharFormat21fontHintingPreferenceEv(
    const QTextCharFormat *self) {
  return self->fontHintingPreference();
}

//  void QTextCharFormat::setFontKerning(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat14setFontKerningEb(
    QTextCharFormat *self,
    bool enable) {
  self->setFontKerning(enable);
}

//  bool QTextCharFormat::fontKerning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTextCharFormat11fontKerningEv(
    const QTextCharFormat *self) {
  return self->fontKerning();
}

//  void QTextCharFormat::setUnderlineStyle(UnderlineStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat17setUnderlineStyleENS_14UnderlineStyleE(
    QTextCharFormat *self,
    QTextCharFormat::UnderlineStyle style) {
  self->setUnderlineStyle(style);
}

//  UnderlineStyle QTextCharFormat::underlineStyle() const
extern "C" Q_DECL_EXPORT
QTextCharFormat::UnderlineStyle ritual_ZNK15QTextCharFormat14underlineStyleEv(
    const QTextCharFormat *self) {
  return self->underlineStyle();
}

//  void QTextCharFormat::setVerticalAlignment(VerticalAlignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat20setVerticalAlignmentENS_17VerticalAlignmentE(
    QTextCharFormat *self,
    QTextCharFormat::VerticalAlignment alignment) {
  self->setVerticalAlignment(alignment);
}

//  VerticalAlignment QTextCharFormat::verticalAlignment() const
extern "C" Q_DECL_EXPORT
QTextCharFormat::VerticalAlignment ritual_ZNK15QTextCharFormat17verticalAlignmentEv(
    const QTextCharFormat *self) {
  return self->verticalAlignment();
}

//  void QTextCharFormat::setTextOutline(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat14setTextOutlineERK4QPen(
    QTextCharFormat *self,
    const QPen *pen) {
  self->setTextOutline(*pen);
}

//  QPen QTextCharFormat::textOutline() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK15QTextCharFormat11textOutlineEv(
    const QTextCharFormat *self) {
  return new QPen(self->textOutline());
}

//  void QTextCharFormat::setToolTip(const QString &tip)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat10setToolTipERK7QString(
    QTextCharFormat *self,
    const QString *tip) {
  self->setToolTip(*tip);
}

//  QString QTextCharFormat::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QTextCharFormat7toolTipEv(const QTextCharFormat *self) {
  return new QString(self->toolTip());
}

//  void QTextCharFormat::setSuperScriptBaseline(qreal baseline)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat22setSuperScriptBaselineEd(
    QTextCharFormat *self,
    qreal baseline) {
  self->setSuperScriptBaseline(baseline);
}

//  qreal QTextCharFormat::superScriptBaseline() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QTextCharFormat19superScriptBaselineEv(
    const QTextCharFormat *self) {
  return self->superScriptBaseline();
}

//  void QTextCharFormat::setSubScriptBaseline(qreal baseline)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat20setSubScriptBaselineEd(
    QTextCharFormat *self,
    qreal baseline) {
  self->setSubScriptBaseline(baseline);
}

//  qreal QTextCharFormat::subScriptBaseline() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QTextCharFormat17subScriptBaselineEv(
    const QTextCharFormat *self) {
  return self->subScriptBaseline();
}

//  void QTextCharFormat::setBaselineOffset(qreal baseline)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat17setBaselineOffsetEd(
    QTextCharFormat *self,
    qreal baseline) {
  self->setBaselineOffset(baseline);
}

//  qreal QTextCharFormat::baselineOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QTextCharFormat14baselineOffsetEv(
    const QTextCharFormat *self) {
  return self->baselineOffset();
}

//  void QTextCharFormat::setAnchor(bool anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat9setAnchorEb(
    QTextCharFormat *self,
    bool anchor) {
  self->setAnchor(anchor);
}

//  bool QTextCharFormat::isAnchor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTextCharFormat8isAnchorEv(const QTextCharFormat *self) {
  return self->isAnchor();
}

//  void QTextCharFormat::setAnchorHref(const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat13setAnchorHrefERK7QString(
    QTextCharFormat *self,
    const QString *value) {
  self->setAnchorHref(*value);
}

//  QString QTextCharFormat::anchorHref() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QTextCharFormat10anchorHrefEv(
    const QTextCharFormat *self) {
  return new QString(self->anchorHref());
}

//  void QTextCharFormat::setAnchorNames(const QStringList &names)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat14setAnchorNamesERK5QListI7QStringE(
    QTextCharFormat *self,
    const QList<QString> *names) {
  self->setAnchorNames(*names);
}

//  QStringList QTextCharFormat::anchorNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QTextCharFormat11anchorNamesEv(
    const QTextCharFormat *self) {
  return new QList<QString>(self->anchorNames());
}

//  void QTextCharFormat::setTableCellRowSpan(int tableCellRowSpan)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat19setTableCellRowSpanEi(
    QTextCharFormat *self,
    int tableCellRowSpan) {
  self->setTableCellRowSpan(tableCellRowSpan);
}

//  int QTextCharFormat::tableCellRowSpan() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextCharFormat16tableCellRowSpanEv(
    const QTextCharFormat *self) {
  return self->tableCellRowSpan();
}

//  void QTextCharFormat::setTableCellColumnSpan(int tableCellColumnSpan)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormat22setTableCellColumnSpanEi(
    QTextCharFormat *self,
    int tableCellColumnSpan) {
  self->setTableCellColumnSpan(tableCellColumnSpan);
}

//  int QTextCharFormat::tableCellColumnSpan() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextCharFormat19tableCellColumnSpanEv(
    const QTextCharFormat *self) {
  return self->tableCellColumnSpan();
}

//  QTextCharFormat::QTextCharFormat(const QTextFormat &fmt)
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZN15QTextCharFormatC1ERK11QTextFormat(
    const QTextFormat *fmt) {
  return new QTextCharFormat(*fmt);
}

//  QTextCharFormat::~QTextCharFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCharFormatD1Ev(QTextCharFormat *self) {
  delete self;
}
