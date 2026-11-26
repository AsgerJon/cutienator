//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(cssparser)
#if !defined(QT_NO_CSSPARSER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcssparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qsize.h>

//  QCss::ValueExtractor::ValueExtractor(const QList<Declaration>
//      &declarations, const QPalette &a1)
extern "C" Q_DECL_EXPORT
QCss::ValueExtractor *ritual_ZN4QCss14ValueExtractorC1ERK5QListINS_11DeclarationEERK8QPalette(
    const QList<QCss::Declaration> *declarations,
    const QPalette *a1) {
  return new QCss::ValueExtractor(*declarations, *a1);
}

//  bool QCss::ValueExtractor::extractFont(QFont *font, int
//      *fontSizeAdjustment)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss14ValueExtractor11extractFontEP5QFontPi(
    QCss::ValueExtractor *self,
    QFont *font,
    int *fontSizeAdjustment) {
  return self->extractFont(font, fontSizeAdjustment);
}

//  bool QCss::ValueExtractor::extractBackground(QBrush *a0, QString *a1,
//      Repeat *a2, Qt::Alignment *a3, QCss::Origin *a4, QCss::Attachment
//      *a5, QCss::Origin *a6) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss14ValueExtractor17extractBackgroundEP6QBrushP7QStringPNS_6RepeatEP6QFlagsIN2Qt13AlignmentFlagEEPNS_6OriginEPNS_10AttachmentESD_(
    const QCss::ValueExtractor *self,
    QBrush *a0,
    QString *a1,
    QCss::Repeat *a2,
    Qt::Alignment *a3,
    QCss::Origin *a4,
    QCss::Attachment *a5,
    QCss::Origin *a6) {
  return self->extractBackground(a0, a1, a2, a3, a4, a5, a6);
}

//  bool QCss::ValueExtractor::extractGeometry(int *w, int *h, int *minw, int
//      *minh, int *maxw, int *maxh)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss14ValueExtractor15extractGeometryEPiS1_S1_S1_S1_S1_(
    QCss::ValueExtractor *self,
    int *w,
    int *h,
    int *minw,
    int *minh,
    int *maxw,
    int *maxh) {
  return self->extractGeometry(w, h, minw, minh, maxw, maxh);
}

//  bool QCss::ValueExtractor::extractPosition(int *l, int *t, int *r, int
//      *b, QCss::Origin *a4, Qt::Alignment *a5, QCss::PositionMode *a6,
//      Qt::Alignment *a7)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss14ValueExtractor15extractPositionEPiS1_S1_S1_PNS_6OriginEP6QFlagsIN2Qt13AlignmentFlagEEPNS_12PositionModeES8_(
    QCss::ValueExtractor *self,
    int *l,
    int *t,
    int *r,
    int *b,
    QCss::Origin *a4,
    Qt::Alignment *a5,
    QCss::PositionMode *a6,
    Qt::Alignment *a7) {
  return self->extractPosition(l, t, r, b, a4, a5, a6, a7);
}

//  bool QCss::ValueExtractor::extractBox(int *margins, int *paddings, int
//      *spacing)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss14ValueExtractor10extractBoxEPiS1_S1_(
    QCss::ValueExtractor *self,
    int *margins,
    int *paddings,
    int *spacing) {
  return self->extractBox(margins, paddings, spacing);
}

//  bool QCss::ValueExtractor::extractBorder(int *borders, QBrush *colors,
//      BorderStyle *Styles, QSize *radii)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss14ValueExtractor13extractBorderEPiP6QBrushPNS_11BorderStyleEP5QSize(
    QCss::ValueExtractor *self,
    int *borders,
    QBrush *colors,
    QCss::BorderStyle *Styles,
    QSize *radii) {
  return self->extractBorder(borders, colors, Styles, radii);
}

//  bool QCss::ValueExtractor::extractOutline(int *borders, QBrush *colors,
//      BorderStyle *Styles, QSize *radii, int *offsets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss14ValueExtractor14extractOutlineEPiP6QBrushPNS_11BorderStyleEP5QSizeS1_(
    QCss::ValueExtractor *self,
    int *borders,
    QBrush *colors,
    QCss::BorderStyle *Styles,
    QSize *radii,
    int *offsets) {
  return self->extractOutline(borders, colors, Styles, radii, offsets);
}

//  bool QCss::ValueExtractor::extractPalette(QBrush *foreground, QBrush
//      *selectedForeground, QBrush *selectedBackground, QBrush
//      *alternateBackground, QBrush *placeHolderTextForeground, QBrush
//      *accent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss14ValueExtractor14extractPaletteEP6QBrushS2_S2_S2_S2_S2_(
    const QCss::ValueExtractor *self,
    QBrush *foreground,
    QBrush *selectedForeground,
    QBrush *selectedBackground,
    QBrush *alternateBackground,
    QBrush *placeHolderTextForeground,
    QBrush *accent) {
  return self->extractPalette(
      foreground,
      selectedForeground,
      selectedBackground,
      alternateBackground,
      placeHolderTextForeground,
      accent);
}

//  int QCss::ValueExtractor::extractStyleFeatures() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QCss14ValueExtractor20extractStyleFeaturesEv(
    const QCss::ValueExtractor *self) {
  return self->extractStyleFeatures();
}

//  bool QCss::ValueExtractor::extractImage(QIcon *icon, Qt::Alignment *a,
//      QSize *size) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss14ValueExtractor12extractImageEP5QIconP6QFlagsIN2Qt13AlignmentFlagEEP5QSize(
    const QCss::ValueExtractor *self,
    QIcon *icon,
    Qt::Alignment *a,
    QSize *size) {
  return self->extractImage(icon, a, size);
}

//  bool QCss::ValueExtractor::extractIcon(QIcon *icon, QSize *size) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss14ValueExtractor11extractIconEP5QIconP5QSize(
    const QCss::ValueExtractor *self,
    QIcon *icon,
    QSize *size) {
  return self->extractIcon(icon, size);
}

//  void QCss::ValueExtractor::lengthValues(const Declaration &decl, int *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss14ValueExtractor12lengthValuesERKNS_11DeclarationEPi(
    QCss::ValueExtractor *self,
    const QCss::Declaration *decl,
    int *m) {
  self->lengthValues(*decl, m);
}

//  QTextLength QCss::ValueExtractor::textLength(const Declaration &decl)
extern "C" Q_DECL_EXPORT
QTextLength *ritual_ZN4QCss14ValueExtractor10textLengthERKNS_11DeclarationE(
    QCss::ValueExtractor *self,
    const QCss::Declaration *decl) {
  return new QTextLength(self->textLength(*decl));
}

//  void QCss::ValueExtractor::extractFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss14ValueExtractor11extractFontEv(
    QCss::ValueExtractor *self) {
  self->extractFont();
}

//  void QCss::ValueExtractor::borderValue(const Declaration &decl, int
//      *width, QCss::BorderStyle *style, QBrush *color)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss14ValueExtractor11borderValueERKNS_11DeclarationEPiPNS_11BorderStyleEP6QBrush(
    QCss::ValueExtractor *self,
    const QCss::Declaration *decl,
    int *width,
    QCss::BorderStyle *style,
    QBrush *color) {
  self->borderValue(*decl, width, style, color);
}

//  LengthData QCss::ValueExtractor::lengthValue(const Value &v)
extern "C" Q_DECL_EXPORT
QCss::LengthData *ritual_ZN4QCss14ValueExtractor11lengthValueERKNS_5ValueE(
    QCss::ValueExtractor *self,
    const QCss::Value *v) {
  return new QCss::LengthData(self->lengthValue(*v));
}

//  int QCss::ValueExtractor::lengthValue(const Declaration &decl)
extern "C" Q_DECL_EXPORT
int ritual_ZN4QCss14ValueExtractor11lengthValueERKNS_11DeclarationE(
    QCss::ValueExtractor *self,
    const QCss::Declaration *decl) {
  return self->lengthValue(*decl);
}

//  QSize QCss::ValueExtractor::sizeValue(const Declaration &decl)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN4QCss14ValueExtractor9sizeValueERKNS_11DeclarationE(
    QCss::ValueExtractor *self,
    const QCss::Declaration *decl) {
  return new QSize(self->sizeValue(*decl));
}

//  void QCss::ValueExtractor::sizeValues(const Declaration &decl, QSize
//      *radii)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss14ValueExtractor10sizeValuesERKNS_11DeclarationEP5QSize(
    QCss::ValueExtractor *self,
    const QCss::Declaration *decl,
    QSize *radii) {
  self->sizeValues(*decl, radii);
}

//  QCss::ValueExtractor::~ValueExtractor()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss14ValueExtractorD1Ev(QCss::ValueExtractor *self) {
  delete self;
}

#endif  // !defined(QT_NO_CSSPARSER)
#endif  // QT_CONFIG(cssparser)
