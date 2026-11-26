//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  DomProperty::DomProperty()
extern "C" Q_DECL_EXPORT
DomProperty *ritual_ZN11DomPropertyC1Ev() {
  return new DomProperty();
}

//  DomProperty::~DomProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomPropertyD1Ev(DomProperty *self) {
  delete self;
}

//  void DomProperty::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty4readER16QXmlStreamReader(
    DomProperty *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomProperty::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11DomProperty5writeER16QXmlStreamWriterRK7QString(
    const DomProperty *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomProperty::hasAttributeName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11DomProperty16hasAttributeNameEv(const DomProperty *self) {
  return self->hasAttributeName();
}

//  QString DomProperty::attributeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11DomProperty13attributeNameEv(const DomProperty *self) {
  return new QString(self->attributeName());
}

//  void DomProperty::setAttributeName(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty16setAttributeNameERK7QString(
    DomProperty *self,
    const QString *a) {
  self->setAttributeName(*a);
}

//  void DomProperty::clearAttributeName()
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty18clearAttributeNameEv(DomProperty *self) {
  self->clearAttributeName();
}

//  bool DomProperty::hasAttributeStdset() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11DomProperty18hasAttributeStdsetEv(const DomProperty *self) {
  return self->hasAttributeStdset();
}

//  int DomProperty::attributeStdset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11DomProperty15attributeStdsetEv(const DomProperty *self) {
  return self->attributeStdset();
}

//  void DomProperty::setAttributeStdset(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty18setAttributeStdsetEi(DomProperty *self, int a) {
  self->setAttributeStdset(a);
}

//  void DomProperty::clearAttributeStdset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty20clearAttributeStdsetEv(DomProperty *self) {
  self->clearAttributeStdset();
}

//  Kind DomProperty::kind() const
extern "C" Q_DECL_EXPORT
DomProperty::Kind ritual_ZNK11DomProperty4kindEv(const DomProperty *self) {
  return self->kind();
}

//  QString DomProperty::elementBool() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11DomProperty11elementBoolEv(const DomProperty *self) {
  return new QString(self->elementBool());
}

//  void DomProperty::setElementBool(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty14setElementBoolERK7QString(
    DomProperty *self,
    const QString *a) {
  self->setElementBool(*a);
}

//  DomColor *DomProperty::elementColor() const
extern "C" Q_DECL_EXPORT
DomColor *ritual_ZNK11DomProperty12elementColorEv(const DomProperty *self) {
  return self->elementColor();
}

//  DomColor *DomProperty::takeElementColor()
extern "C" Q_DECL_EXPORT
DomColor *ritual_ZN11DomProperty16takeElementColorEv(DomProperty *self) {
  return self->takeElementColor();
}

//  void DomProperty::setElementColor(DomColor *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty15setElementColorEP8DomColor(
    DomProperty *self,
    DomColor *a) {
  self->setElementColor(a);
}

//  QString DomProperty::elementCstring() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11DomProperty14elementCstringEv(const DomProperty *self) {
  return new QString(self->elementCstring());
}

//  void DomProperty::setElementCstring(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty17setElementCstringERK7QString(
    DomProperty *self,
    const QString *a) {
  self->setElementCstring(*a);
}

//  int DomProperty::elementCursor() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11DomProperty13elementCursorEv(const DomProperty *self) {
  return self->elementCursor();
}

//  void DomProperty::setElementCursor(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty16setElementCursorEi(DomProperty *self, int a) {
  self->setElementCursor(a);
}

//  QString DomProperty::elementCursorShape() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11DomProperty18elementCursorShapeEv(
    const DomProperty *self) {
  return new QString(self->elementCursorShape());
}

//  void DomProperty::setElementCursorShape(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty21setElementCursorShapeERK7QString(
    DomProperty *self,
    const QString *a) {
  self->setElementCursorShape(*a);
}

//  QString DomProperty::elementEnum() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11DomProperty11elementEnumEv(const DomProperty *self) {
  return new QString(self->elementEnum());
}

//  void DomProperty::setElementEnum(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty14setElementEnumERK7QString(
    DomProperty *self,
    const QString *a) {
  self->setElementEnum(*a);
}

//  DomFont *DomProperty::elementFont() const
extern "C" Q_DECL_EXPORT
DomFont *ritual_ZNK11DomProperty11elementFontEv(const DomProperty *self) {
  return self->elementFont();
}

//  DomFont *DomProperty::takeElementFont()
extern "C" Q_DECL_EXPORT
DomFont *ritual_ZN11DomProperty15takeElementFontEv(DomProperty *self) {
  return self->takeElementFont();
}

//  void DomProperty::setElementFont(DomFont *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty14setElementFontEP7DomFont(
    DomProperty *self,
    DomFont *a) {
  self->setElementFont(a);
}

//  DomResourceIcon *DomProperty::elementIconSet() const
extern "C" Q_DECL_EXPORT
DomResourceIcon *ritual_ZNK11DomProperty14elementIconSetEv(
    const DomProperty *self) {
  return self->elementIconSet();
}

//  DomResourceIcon *DomProperty::takeElementIconSet()
extern "C" Q_DECL_EXPORT
DomResourceIcon *ritual_ZN11DomProperty18takeElementIconSetEv(
    DomProperty *self) {
  return self->takeElementIconSet();
}

//  void DomProperty::setElementIconSet(DomResourceIcon *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty17setElementIconSetEP15DomResourceIcon(
    DomProperty *self,
    DomResourceIcon *a) {
  self->setElementIconSet(a);
}

//  DomResourcePixmap *DomProperty::elementPixmap() const
extern "C" Q_DECL_EXPORT
DomResourcePixmap *ritual_ZNK11DomProperty13elementPixmapEv(
    const DomProperty *self) {
  return self->elementPixmap();
}

//  DomResourcePixmap *DomProperty::takeElementPixmap()
extern "C" Q_DECL_EXPORT
DomResourcePixmap *ritual_ZN11DomProperty17takeElementPixmapEv(
    DomProperty *self) {
  return self->takeElementPixmap();
}

//  void DomProperty::setElementPixmap(DomResourcePixmap *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty16setElementPixmapEP17DomResourcePixmap(
    DomProperty *self,
    DomResourcePixmap *a) {
  self->setElementPixmap(a);
}

//  DomPalette *DomProperty::elementPalette() const
extern "C" Q_DECL_EXPORT
DomPalette *ritual_ZNK11DomProperty14elementPaletteEv(
    const DomProperty *self) {
  return self->elementPalette();
}

//  DomPalette *DomProperty::takeElementPalette()
extern "C" Q_DECL_EXPORT
DomPalette *ritual_ZN11DomProperty18takeElementPaletteEv(DomProperty *self) {
  return self->takeElementPalette();
}

//  void DomProperty::setElementPalette(DomPalette *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty17setElementPaletteEP10DomPalette(
    DomProperty *self,
    DomPalette *a) {
  self->setElementPalette(a);
}

//  DomPoint *DomProperty::elementPoint() const
extern "C" Q_DECL_EXPORT
DomPoint *ritual_ZNK11DomProperty12elementPointEv(const DomProperty *self) {
  return self->elementPoint();
}

//  DomPoint *DomProperty::takeElementPoint()
extern "C" Q_DECL_EXPORT
DomPoint *ritual_ZN11DomProperty16takeElementPointEv(DomProperty *self) {
  return self->takeElementPoint();
}

//  void DomProperty::setElementPoint(DomPoint *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty15setElementPointEP8DomPoint(
    DomProperty *self,
    DomPoint *a) {
  self->setElementPoint(a);
}

//  DomRect *DomProperty::elementRect() const
extern "C" Q_DECL_EXPORT
DomRect *ritual_ZNK11DomProperty11elementRectEv(const DomProperty *self) {
  return self->elementRect();
}

//  DomRect *DomProperty::takeElementRect()
extern "C" Q_DECL_EXPORT
DomRect *ritual_ZN11DomProperty15takeElementRectEv(DomProperty *self) {
  return self->takeElementRect();
}

//  void DomProperty::setElementRect(DomRect *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty14setElementRectEP7DomRect(
    DomProperty *self,
    DomRect *a) {
  self->setElementRect(a);
}

//  QString DomProperty::elementSet() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11DomProperty10elementSetEv(const DomProperty *self) {
  return new QString(self->elementSet());
}

//  void DomProperty::setElementSet(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty13setElementSetERK7QString(
    DomProperty *self,
    const QString *a) {
  self->setElementSet(*a);
}

//  DomLocale *DomProperty::elementLocale() const
extern "C" Q_DECL_EXPORT
DomLocale *ritual_ZNK11DomProperty13elementLocaleEv(
    const DomProperty *self) {
  return self->elementLocale();
}

//  DomLocale *DomProperty::takeElementLocale()
extern "C" Q_DECL_EXPORT
DomLocale *ritual_ZN11DomProperty17takeElementLocaleEv(DomProperty *self) {
  return self->takeElementLocale();
}

//  void DomProperty::setElementLocale(DomLocale *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty16setElementLocaleEP9DomLocale(
    DomProperty *self,
    DomLocale *a) {
  self->setElementLocale(a);
}

//  DomSizePolicy *DomProperty::elementSizePolicy() const
extern "C" Q_DECL_EXPORT
DomSizePolicy *ritual_ZNK11DomProperty17elementSizePolicyEv(
    const DomProperty *self) {
  return self->elementSizePolicy();
}

//  DomSizePolicy *DomProperty::takeElementSizePolicy()
extern "C" Q_DECL_EXPORT
DomSizePolicy *ritual_ZN11DomProperty21takeElementSizePolicyEv(
    DomProperty *self) {
  return self->takeElementSizePolicy();
}

//  void DomProperty::setElementSizePolicy(DomSizePolicy *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty20setElementSizePolicyEP13DomSizePolicy(
    DomProperty *self,
    DomSizePolicy *a) {
  self->setElementSizePolicy(a);
}

//  DomSize *DomProperty::elementSize() const
extern "C" Q_DECL_EXPORT
DomSize *ritual_ZNK11DomProperty11elementSizeEv(const DomProperty *self) {
  return self->elementSize();
}

//  DomSize *DomProperty::takeElementSize()
extern "C" Q_DECL_EXPORT
DomSize *ritual_ZN11DomProperty15takeElementSizeEv(DomProperty *self) {
  return self->takeElementSize();
}

//  void DomProperty::setElementSize(DomSize *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty14setElementSizeEP7DomSize(
    DomProperty *self,
    DomSize *a) {
  self->setElementSize(a);
}

//  DomString *DomProperty::elementString() const
extern "C" Q_DECL_EXPORT
DomString *ritual_ZNK11DomProperty13elementStringEv(
    const DomProperty *self) {
  return self->elementString();
}

//  DomString *DomProperty::takeElementString()
extern "C" Q_DECL_EXPORT
DomString *ritual_ZN11DomProperty17takeElementStringEv(DomProperty *self) {
  return self->takeElementString();
}

//  void DomProperty::setElementString(DomString *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty16setElementStringEP9DomString(
    DomProperty *self,
    DomString *a) {
  self->setElementString(a);
}

//  DomStringList *DomProperty::elementStringList() const
extern "C" Q_DECL_EXPORT
DomStringList *ritual_ZNK11DomProperty17elementStringListEv(
    const DomProperty *self) {
  return self->elementStringList();
}

//  DomStringList *DomProperty::takeElementStringList()
extern "C" Q_DECL_EXPORT
DomStringList *ritual_ZN11DomProperty21takeElementStringListEv(
    DomProperty *self) {
  return self->takeElementStringList();
}

//  void DomProperty::setElementStringList(DomStringList *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty20setElementStringListEP13DomStringList(
    DomProperty *self,
    DomStringList *a) {
  self->setElementStringList(a);
}

//  int DomProperty::elementNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11DomProperty13elementNumberEv(const DomProperty *self) {
  return self->elementNumber();
}

//  void DomProperty::setElementNumber(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty16setElementNumberEi(DomProperty *self, int a) {
  self->setElementNumber(a);
}

//  float DomProperty::elementFloat() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11DomProperty12elementFloatEv(const DomProperty *self) {
  return self->elementFloat();
}

//  void DomProperty::setElementFloat(float a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty15setElementFloatEf(DomProperty *self, float a) {
  self->setElementFloat(a);
}

//  double DomProperty::elementDouble() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK11DomProperty13elementDoubleEv(const DomProperty *self) {
  return self->elementDouble();
}

//  void DomProperty::setElementDouble(double a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty16setElementDoubleEd(
    DomProperty *self,
    double a) {
  self->setElementDouble(a);
}

//  DomDate *DomProperty::elementDate() const
extern "C" Q_DECL_EXPORT
DomDate *ritual_ZNK11DomProperty11elementDateEv(const DomProperty *self) {
  return self->elementDate();
}

//  DomDate *DomProperty::takeElementDate()
extern "C" Q_DECL_EXPORT
DomDate *ritual_ZN11DomProperty15takeElementDateEv(DomProperty *self) {
  return self->takeElementDate();
}

//  void DomProperty::setElementDate(DomDate *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty14setElementDateEP7DomDate(
    DomProperty *self,
    DomDate *a) {
  self->setElementDate(a);
}

//  DomTime *DomProperty::elementTime() const
extern "C" Q_DECL_EXPORT
DomTime *ritual_ZNK11DomProperty11elementTimeEv(const DomProperty *self) {
  return self->elementTime();
}

//  DomTime *DomProperty::takeElementTime()
extern "C" Q_DECL_EXPORT
DomTime *ritual_ZN11DomProperty15takeElementTimeEv(DomProperty *self) {
  return self->takeElementTime();
}

//  void DomProperty::setElementTime(DomTime *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty14setElementTimeEP7DomTime(
    DomProperty *self,
    DomTime *a) {
  self->setElementTime(a);
}

//  DomDateTime *DomProperty::elementDateTime() const
extern "C" Q_DECL_EXPORT
DomDateTime *ritual_ZNK11DomProperty15elementDateTimeEv(
    const DomProperty *self) {
  return self->elementDateTime();
}

//  DomDateTime *DomProperty::takeElementDateTime()
extern "C" Q_DECL_EXPORT
DomDateTime *ritual_ZN11DomProperty19takeElementDateTimeEv(
    DomProperty *self) {
  return self->takeElementDateTime();
}

//  void DomProperty::setElementDateTime(DomDateTime *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty18setElementDateTimeEP11DomDateTime(
    DomProperty *self,
    DomDateTime *a) {
  self->setElementDateTime(a);
}

//  DomPointF *DomProperty::elementPointF() const
extern "C" Q_DECL_EXPORT
DomPointF *ritual_ZNK11DomProperty13elementPointFEv(
    const DomProperty *self) {
  return self->elementPointF();
}

//  DomPointF *DomProperty::takeElementPointF()
extern "C" Q_DECL_EXPORT
DomPointF *ritual_ZN11DomProperty17takeElementPointFEv(DomProperty *self) {
  return self->takeElementPointF();
}

//  void DomProperty::setElementPointF(DomPointF *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty16setElementPointFEP9DomPointF(
    DomProperty *self,
    DomPointF *a) {
  self->setElementPointF(a);
}

//  DomRectF *DomProperty::elementRectF() const
extern "C" Q_DECL_EXPORT
DomRectF *ritual_ZNK11DomProperty12elementRectFEv(const DomProperty *self) {
  return self->elementRectF();
}

//  DomRectF *DomProperty::takeElementRectF()
extern "C" Q_DECL_EXPORT
DomRectF *ritual_ZN11DomProperty16takeElementRectFEv(DomProperty *self) {
  return self->takeElementRectF();
}

//  void DomProperty::setElementRectF(DomRectF *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty15setElementRectFEP8DomRectF(
    DomProperty *self,
    DomRectF *a) {
  self->setElementRectF(a);
}

//  DomSizeF *DomProperty::elementSizeF() const
extern "C" Q_DECL_EXPORT
DomSizeF *ritual_ZNK11DomProperty12elementSizeFEv(const DomProperty *self) {
  return self->elementSizeF();
}

//  DomSizeF *DomProperty::takeElementSizeF()
extern "C" Q_DECL_EXPORT
DomSizeF *ritual_ZN11DomProperty16takeElementSizeFEv(DomProperty *self) {
  return self->takeElementSizeF();
}

//  void DomProperty::setElementSizeF(DomSizeF *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty15setElementSizeFEP8DomSizeF(
    DomProperty *self,
    DomSizeF *a) {
  self->setElementSizeF(a);
}

//  qlonglong DomProperty::elementLongLong() const
extern "C" Q_DECL_EXPORT
qlonglong ritual_ZNK11DomProperty15elementLongLongEv(
    const DomProperty *self) {
  return self->elementLongLong();
}

//  void DomProperty::setElementLongLong(qlonglong a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty18setElementLongLongEx(
    DomProperty *self,
    qlonglong a) {
  self->setElementLongLong(a);
}

//  DomChar *DomProperty::elementChar() const
extern "C" Q_DECL_EXPORT
DomChar *ritual_ZNK11DomProperty11elementCharEv(const DomProperty *self) {
  return self->elementChar();
}

//  DomChar *DomProperty::takeElementChar()
extern "C" Q_DECL_EXPORT
DomChar *ritual_ZN11DomProperty15takeElementCharEv(DomProperty *self) {
  return self->takeElementChar();
}

//  void DomProperty::setElementChar(DomChar *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty14setElementCharEP7DomChar(
    DomProperty *self,
    DomChar *a) {
  self->setElementChar(a);
}

//  DomUrl *DomProperty::elementUrl() const
extern "C" Q_DECL_EXPORT
DomUrl *ritual_ZNK11DomProperty10elementUrlEv(const DomProperty *self) {
  return self->elementUrl();
}

//  DomUrl *DomProperty::takeElementUrl()
extern "C" Q_DECL_EXPORT
DomUrl *ritual_ZN11DomProperty14takeElementUrlEv(DomProperty *self) {
  return self->takeElementUrl();
}

//  void DomProperty::setElementUrl(DomUrl *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty13setElementUrlEP6DomUrl(
    DomProperty *self,
    DomUrl *a) {
  self->setElementUrl(a);
}

//  uint DomProperty::elementUInt() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK11DomProperty11elementUIntEv(const DomProperty *self) {
  return self->elementUInt();
}

//  void DomProperty::setElementUInt(uint a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty14setElementUIntEj(DomProperty *self, uint a) {
  self->setElementUInt(a);
}

//  qulonglong DomProperty::elementULongLong() const
extern "C" Q_DECL_EXPORT
qulonglong ritual_ZNK11DomProperty16elementULongLongEv(
    const DomProperty *self) {
  return self->elementULongLong();
}

//  void DomProperty::setElementULongLong(qulonglong a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty19setElementULongLongEy(
    DomProperty *self,
    qulonglong a) {
  self->setElementULongLong(a);
}

//  DomBrush *DomProperty::elementBrush() const
extern "C" Q_DECL_EXPORT
DomBrush *ritual_ZNK11DomProperty12elementBrushEv(const DomProperty *self) {
  return self->elementBrush();
}

//  DomBrush *DomProperty::takeElementBrush()
extern "C" Q_DECL_EXPORT
DomBrush *ritual_ZN11DomProperty16takeElementBrushEv(DomProperty *self) {
  return self->takeElementBrush();
}

//  void DomProperty::setElementBrush(DomBrush *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty15setElementBrushEP8DomBrush(
    DomProperty *self,
    DomBrush *a) {
  self->setElementBrush(a);
}

//  void DomProperty::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomProperty5clearEv(DomProperty *self) {
  self->clear();
}

//  QList<DomProperty *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_list_make_DomProperty_ptr() {
  return new QList<DomProperty *>();
}

//  void QList<DomProperty *>::append(const DomProperty * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomProperty_ptr(
    QList<DomProperty *> *self,
    DomProperty *element) {
  self->append(element);
}

//  qsizetype QList<DomProperty *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomProperty_ptr(
    const QList<DomProperty *> *self) {
  return self->size();
}

//  const DomProperty * &QList<DomProperty *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomProperty *ritual_list_at_DomProperty_ptr(
    const QList<DomProperty *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomProperty *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomProperty_ptr(QList<DomProperty *> *self) {
  delete self;
}
