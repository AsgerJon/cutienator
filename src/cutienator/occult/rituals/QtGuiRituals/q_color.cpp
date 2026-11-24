//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qcolor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qcolor.h>
#include <QtGui/qrgba64.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QColor::QColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColorC1Ev() {
  return new QColor();
}

//  QColor::QColor(Qt::GlobalColor color)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColorC1EN2Qt11GlobalColorE(Qt::GlobalColor color) {
  return new QColor(color);
}

//  QColor::QColor(int r, int g, int b, int a)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColorC1Eiiii(int r, int g, int b, int a) {
  return new QColor(r, g, b, a);
}

//  QColor::QColor(QRgb rgb)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColorC1Ej(QRgb rgb) {
  return new QColor(rgb);
}

//  QColor::QColor(QRgba64 rgba64)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColorC1E7QRgba64(const QRgba64 *rgba64) {
  return new QColor(*rgba64);
}

//  QColor::QColor(const QString &name)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColorC1ERK7QString(const QString *name) {
  return new QColor(*name);
}

//  QColor::QColor(QStringView name)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColorC1E11QStringView(const QString *name) {
  return new QColor(QStringView(*name));
}

//  QColor::QColor(const char *aname)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColorC1EPKc(const char *aname) {
  return new QColor(aname);
}

//  QColor::QColor(QLatin1StringView name)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColorC1E13QLatin1String(const QLatin1String *name) {
  return new QColor(*name);
}

//  QColor::QColor(Spec spec)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColorC1ENS_4SpecE(QColor::Spec spec) {
  return new QColor(spec);
}

//  QColor QColor::fromString(QAnyStringView name)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor10fromStringE14QAnyStringView(const QString *name) {
  return new QColor(QColor::fromString(QAnyStringView(*name)));
}

//  bool QColor::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QColor7isValidEv(const QColor *self) {
  return self->isValid();
}

//  QString QColor::name(NameFormat format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QColor4nameENS_10NameFormatE(
    const QColor *self,
    QColor::NameFormat format) {
  return new QString(self->name(format));
}

#if QT_DEPRECATED_SINCE(6, 6)
//  void QColor::setNamedColor(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor13setNamedColorERK7QString(
    QColor *self,
    const QString *name) {
  self->setNamedColor(*name);
}
#endif  // QT_DEPRECATED_SINCE(6, 6)

#if QT_DEPRECATED_SINCE(6, 6)
//  void QColor::setNamedColor(QStringView name)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor13setNamedColorE11QStringView(
    QColor *self,
    const QString *name) {
  self->setNamedColor(QStringView(*name));
}
#endif  // QT_DEPRECATED_SINCE(6, 6)

#if QT_DEPRECATED_SINCE(6, 6)
//  void QColor::setNamedColor(QLatin1StringView name)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor13setNamedColorE13QLatin1String(
    QColor *self,
    const QLatin1String *name) {
  self->setNamedColor(*name);
}
#endif  // QT_DEPRECATED_SINCE(6, 6)

//  QStringList QColor::colorNames()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN6QColor10colorNamesEv() {
  return new QList<QString>(QColor::colorNames());
}

//  Spec QColor::spec() const
extern "C" Q_DECL_EXPORT
QColor::Spec ritual_ZNK6QColor4specEv(const QColor *self) {
  return self->spec();
}

//  int QColor::alpha() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor5alphaEv(const QColor *self) {
  return self->alpha();
}

//  void QColor::setAlpha(int alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor8setAlphaEi(QColor *self, int alpha) {
  self->setAlpha(alpha);
}

//  float QColor::alphaF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor6alphaFEv(const QColor *self) {
  return self->alphaF();
}

//  void QColor::setAlphaF(float alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor9setAlphaFEf(QColor *self, float alpha) {
  self->setAlphaF(alpha);
}

//  int QColor::red() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor3redEv(const QColor *self) {
  return self->red();
}

//  int QColor::green() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor5greenEv(const QColor *self) {
  return self->green();
}

//  int QColor::blue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor4blueEv(const QColor *self) {
  return self->blue();
}

//  void QColor::setRed(int red)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor6setRedEi(QColor *self, int red) {
  self->setRed(red);
}

//  void QColor::setGreen(int green)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor8setGreenEi(QColor *self, int green) {
  self->setGreen(green);
}

//  void QColor::setBlue(int blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor7setBlueEi(QColor *self, int blue) {
  self->setBlue(blue);
}

//  float QColor::redF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor4redFEv(const QColor *self) {
  return self->redF();
}

//  float QColor::greenF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor6greenFEv(const QColor *self) {
  return self->greenF();
}

//  float QColor::blueF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor5blueFEv(const QColor *self) {
  return self->blueF();
}

//  void QColor::setRedF(float red)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor7setRedFEf(QColor *self, float red) {
  self->setRedF(red);
}

//  void QColor::setGreenF(float green)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor9setGreenFEf(QColor *self, float green) {
  self->setGreenF(green);
}

//  void QColor::setBlueF(float blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor8setBlueFEf(QColor *self, float blue) {
  self->setBlueF(blue);
}

//  void QColor::getRgb(int *r, int *g, int *b, int *a) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QColor6getRgbEPiS0_S0_S0_(
    const QColor *self,
    int *r,
    int *g,
    int *b,
    int *a) {
  self->getRgb(r, g, b, a);
}

//  void QColor::setRgb(int r, int g, int b, int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor6setRgbEiiii(QColor *self, int r, int g, int b, int a) {
  self->setRgb(r, g, b, a);
}

//  void QColor::getRgbF(float *r, float *g, float *b, float *a) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QColor7getRgbFEPfS0_S0_S0_(
    const QColor *self,
    float *r,
    float *g,
    float *b,
    float *a) {
  self->getRgbF(r, g, b, a);
}

//  void QColor::setRgbF(float r, float g, float b, float a)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor7setRgbFEffff(
    QColor *self,
    float r,
    float g,
    float b,
    float a) {
  self->setRgbF(r, g, b, a);
}

//  QRgba64 QColor::rgba64() const
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZNK6QColor6rgba64Ev(const QColor *self) {
  return new QRgba64(self->rgba64());
}

//  void QColor::setRgba64(QRgba64 rgba)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor9setRgba64E7QRgba64(QColor *self, const QRgba64 *rgba) {
  self->setRgba64(*rgba);
}

//  QRgb QColor::rgba() const
extern "C" Q_DECL_EXPORT
QRgb ritual_ZNK6QColor4rgbaEv(const QColor *self) {
  return self->rgba();
}

//  void QColor::setRgba(QRgb rgba)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor7setRgbaEj(QColor *self, QRgb rgba) {
  self->setRgba(rgba);
}

//  QRgb QColor::rgb() const
extern "C" Q_DECL_EXPORT
QRgb ritual_ZNK6QColor3rgbEv(const QColor *self) {
  return self->rgb();
}

//  void QColor::setRgb(QRgb rgb)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor6setRgbEj(QColor *self, QRgb rgb) {
  self->setRgb(rgb);
}

//  int QColor::hue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor3hueEv(const QColor *self) {
  return self->hue();
}

//  int QColor::saturation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor10saturationEv(const QColor *self) {
  return self->saturation();
}

//  int QColor::hsvHue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor6hsvHueEv(const QColor *self) {
  return self->hsvHue();
}

//  int QColor::hsvSaturation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor13hsvSaturationEv(const QColor *self) {
  return self->hsvSaturation();
}

//  int QColor::value() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor5valueEv(const QColor *self) {
  return self->value();
}

//  float QColor::hueF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor4hueFEv(const QColor *self) {
  return self->hueF();
}

//  float QColor::saturationF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor11saturationFEv(const QColor *self) {
  return self->saturationF();
}

//  float QColor::hsvHueF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor7hsvHueFEv(const QColor *self) {
  return self->hsvHueF();
}

//  float QColor::hsvSaturationF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor14hsvSaturationFEv(const QColor *self) {
  return self->hsvSaturationF();
}

//  float QColor::valueF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor6valueFEv(const QColor *self) {
  return self->valueF();
}

//  void QColor::getHsv(int *h, int *s, int *v, int *a) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QColor6getHsvEPiS0_S0_S0_(
    const QColor *self,
    int *h,
    int *s,
    int *v,
    int *a) {
  self->getHsv(h, s, v, a);
}

//  void QColor::setHsv(int h, int s, int v, int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor6setHsvEiiii(QColor *self, int h, int s, int v, int a) {
  self->setHsv(h, s, v, a);
}

//  void QColor::getHsvF(float *h, float *s, float *v, float *a) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QColor7getHsvFEPfS0_S0_S0_(
    const QColor *self,
    float *h,
    float *s,
    float *v,
    float *a) {
  self->getHsvF(h, s, v, a);
}

//  void QColor::setHsvF(float h, float s, float v, float a)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor7setHsvFEffff(
    QColor *self,
    float h,
    float s,
    float v,
    float a) {
  self->setHsvF(h, s, v, a);
}

//  int QColor::cyan() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor4cyanEv(const QColor *self) {
  return self->cyan();
}

//  int QColor::magenta() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor7magentaEv(const QColor *self) {
  return self->magenta();
}

//  int QColor::yellow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor6yellowEv(const QColor *self) {
  return self->yellow();
}

//  int QColor::black() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor5blackEv(const QColor *self) {
  return self->black();
}

//  float QColor::cyanF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor5cyanFEv(const QColor *self) {
  return self->cyanF();
}

//  float QColor::magentaF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor8magentaFEv(const QColor *self) {
  return self->magentaF();
}

//  float QColor::yellowF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor7yellowFEv(const QColor *self) {
  return self->yellowF();
}

//  float QColor::blackF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor6blackFEv(const QColor *self) {
  return self->blackF();
}

//  void QColor::getCmyk(int *c, int *m, int *y, int *k, int *a) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QColor7getCmykEPiS0_S0_S0_S0_(
    const QColor *self,
    int *c,
    int *m,
    int *y,
    int *k,
    int *a) {
  self->getCmyk(c, m, y, k, a);
}

//  void QColor::setCmyk(int c, int m, int y, int k, int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor7setCmykEiiiii(
    QColor *self,
    int c,
    int m,
    int y,
    int k,
    int a) {
  self->setCmyk(c, m, y, k, a);
}

//  void QColor::getCmykF(float *c, float *m, float *y, float *k, float *a)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QColor8getCmykFEPfS0_S0_S0_S0_(
    const QColor *self,
    float *c,
    float *m,
    float *y,
    float *k,
    float *a) {
  self->getCmykF(c, m, y, k, a);
}

//  void QColor::setCmykF(float c, float m, float y, float k, float a)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor8setCmykFEfffff(
    QColor *self,
    float c,
    float m,
    float y,
    float k,
    float a) {
  self->setCmykF(c, m, y, k, a);
}

//  int QColor::hslHue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor6hslHueEv(const QColor *self) {
  return self->hslHue();
}

//  int QColor::hslSaturation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor13hslSaturationEv(const QColor *self) {
  return self->hslSaturation();
}

//  int QColor::lightness() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QColor9lightnessEv(const QColor *self) {
  return self->lightness();
}

//  float QColor::hslHueF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor7hslHueFEv(const QColor *self) {
  return self->hslHueF();
}

//  float QColor::hslSaturationF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor14hslSaturationFEv(const QColor *self) {
  return self->hslSaturationF();
}

//  float QColor::lightnessF() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK6QColor10lightnessFEv(const QColor *self) {
  return self->lightnessF();
}

//  void QColor::getHsl(int *h, int *s, int *l, int *a) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QColor6getHslEPiS0_S0_S0_(
    const QColor *self,
    int *h,
    int *s,
    int *l,
    int *a) {
  self->getHsl(h, s, l, a);
}

//  void QColor::setHsl(int h, int s, int l, int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor6setHslEiiii(QColor *self, int h, int s, int l, int a) {
  self->setHsl(h, s, l, a);
}

//  void QColor::getHslF(float *h, float *s, float *l, float *a) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QColor7getHslFEPfS0_S0_S0_(
    const QColor *self,
    float *h,
    float *s,
    float *l,
    float *a) {
  self->getHslF(h, s, l, a);
}

//  void QColor::setHslF(float h, float s, float l, float a)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor7setHslFEffff(
    QColor *self,
    float h,
    float s,
    float l,
    float a) {
  self->setHslF(h, s, l, a);
}

//  QColor QColor::toRgb() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QColor5toRgbEv(const QColor *self) {
  return new QColor(self->toRgb());
}

//  QColor QColor::toHsv() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QColor5toHsvEv(const QColor *self) {
  return new QColor(self->toHsv());
}

//  QColor QColor::toCmyk() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QColor6toCmykEv(const QColor *self) {
  return new QColor(self->toCmyk());
}

//  QColor QColor::toHsl() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QColor5toHslEv(const QColor *self) {
  return new QColor(self->toHsl());
}

//  QColor QColor::toExtendedRgb() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QColor13toExtendedRgbEv(const QColor *self) {
  return new QColor(self->toExtendedRgb());
}

//  QColor QColor::convertTo(Spec colorSpec) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QColor9convertToENS_4SpecE(
    const QColor *self,
    QColor::Spec colorSpec) {
  return new QColor(self->convertTo(colorSpec));
}

//  QColor QColor::fromRgb(QRgb rgb)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor7fromRgbEj(QRgb rgb) {
  return new QColor(QColor::fromRgb(rgb));
}

//  QColor QColor::fromRgba(QRgb rgba)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor8fromRgbaEj(QRgb rgba) {
  return new QColor(QColor::fromRgba(rgba));
}

//  QColor QColor::fromRgb(int r, int g, int b, int a)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor7fromRgbEiiii(int r, int g, int b, int a) {
  return new QColor(QColor::fromRgb(r, g, b, a));
}

//  QColor QColor::fromRgbF(float r, float g, float b, float a)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor8fromRgbFEffff(float r, float g, float b, float a) {
  return new QColor(QColor::fromRgbF(r, g, b, a));
}

//  QColor QColor::fromRgba64(ushort r, ushort g, ushort b, ushort a)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor10fromRgba64Etttt(
    ushort r,
    ushort g,
    ushort b,
    ushort a) {
  return new QColor(QColor::fromRgba64(r, g, b, a));
}

//  QColor QColor::fromRgba64(QRgba64 rgba)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor10fromRgba64E7QRgba64(const QRgba64 *rgba) {
  return new QColor(QColor::fromRgba64(*rgba));
}

//  QColor QColor::fromHsv(int h, int s, int v, int a)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor7fromHsvEiiii(int h, int s, int v, int a) {
  return new QColor(QColor::fromHsv(h, s, v, a));
}

//  QColor QColor::fromHsvF(float h, float s, float v, float a)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor8fromHsvFEffff(float h, float s, float v, float a) {
  return new QColor(QColor::fromHsvF(h, s, v, a));
}

//  QColor QColor::fromCmyk(int c, int m, int y, int k, int a)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor8fromCmykEiiiii(int c, int m, int y, int k, int a) {
  return new QColor(QColor::fromCmyk(c, m, y, k, a));
}

//  QColor QColor::fromCmykF(float c, float m, float y, float k, float a)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor9fromCmykFEfffff(
    float c,
    float m,
    float y,
    float k,
    float a) {
  return new QColor(QColor::fromCmykF(c, m, y, k, a));
}

//  QColor QColor::fromHsl(int h, int s, int l, int a)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor7fromHslEiiii(int h, int s, int l, int a) {
  return new QColor(QColor::fromHsl(h, s, l, a));
}

//  QColor QColor::fromHslF(float h, float s, float l, float a)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColor8fromHslFEffff(float h, float s, float l, float a) {
  return new QColor(QColor::fromHslF(h, s, l, a));
}

//  QColor QColor::lighter(int f) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QColor7lighterEi(const QColor *self, int f) {
  return new QColor(self->lighter(f));
}

//  QColor QColor::darker(int f) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QColor6darkerEi(const QColor *self, int f) {
  return new QColor(self->darker(f));
}

//  bool QColor::operator==(const QColor &c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QColoreqERKS_(const QColor *self, const QColor *c) {
  return self->operator==(*c);
}

//  bool QColor::operator!=(const QColor &c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QColorneERKS_(const QColor *self, const QColor *c) {
  return self->operator!=(*c);
}

//  QVariant QColor::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK6QColorcv8QVariantEv(const QColor *self) {
  return new QVariant(self->operator QVariant());
}

#if QT_DEPRECATED_SINCE(6, 6)
//  bool QColor::isValidColor(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QColor12isValidColorERK7QString(const QString *name) {
  return QColor::isValidColor(*name);
}
#endif  // QT_DEPRECATED_SINCE(6, 6)

#if QT_DEPRECATED_SINCE(6, 6)
//  bool QColor::isValidColor(QStringView a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QColor12isValidColorE11QStringView(const QString *a0) {
  return QColor::isValidColor(QStringView(*a0));
}
#endif  // QT_DEPRECATED_SINCE(6, 6)

#if QT_DEPRECATED_SINCE(6, 6)
//  bool QColor::isValidColor(QLatin1StringView a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QColor12isValidColorE13QLatin1String(
    const QLatin1String *a0) {
  return QColor::isValidColor(*a0);
}
#endif  // QT_DEPRECATED_SINCE(6, 6)

//  bool QColor::isValidColorName(QAnyStringView a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QColor16isValidColorNameE14QAnyStringView(const QString *a0) {
  return QColor::isValidColorName(QAnyStringView(*a0));
}

//  void QColor::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColor10invalidateEv(QColor *self) {
  self->invalidate();
}

//  bool QColor::isRgbaValid(int r, int g, int b, int a)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QColor11isRgbaValidEiiii(int r, int g, int b, int a) {
  return QColor::isRgbaValid(r, g, b, a);
}

#if defined(Q_COMPILER_UNIFORM_INIT)
//  QColor::QColor(Spec spec, ushort a1, ushort a2, ushort a3, ushort a4,
//      ushort a5)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN6QColorC1ENS_4SpecEttttt(
    QColor::Spec spec,
    ushort a1,
    ushort a2,
    ushort a3,
    ushort a4,
    ushort a5) {
  return new QColor(spec, a1, a2, a3, a4, a5);
}
#endif  // defined(Q_COMPILER_UNIFORM_INIT)

//  QColor::~QColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QColorD1Ev(QColor *self) {
  delete self;
}

//  QList<QColor>::QList()
extern "C" Q_DECL_EXPORT
QList<QColor> *ritual_list_make_QColor() {
  return new QList<QColor>();
}

//  void QList<QColor>::append(const QColor &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QColor(QList<QColor> *self, const QColor *element) {
  self->append(*element);
}

//  qsizetype QList<QColor>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QColor(const QList<QColor> *self) {
  return self->size();
}

//  const QColor &QList<QColor>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QColor *ritual_list_at_QColor(const QList<QColor> *self, long long index) {
  return new QColor(self->at(index));
}

//  QList<QColor>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QColor(QList<QColor> *self) {
  delete self;
}
