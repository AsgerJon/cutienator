//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextformat.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QTextFormat::QTextFormat()
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_ZN11QTextFormatC1Ev() {
  return new QTextFormat();
}

//  QTextFormat::QTextFormat(int type)
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_ZN11QTextFormatC1Ei(int type) {
  return new QTextFormat(type);
}

//  QTextFormat::QTextFormat(const QTextFormat &rhs)
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_ZN11QTextFormatC1ERKS_(const QTextFormat *rhs) {
  return new QTextFormat(*rhs);
}

//  QTextFormat::~QTextFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormatD1Ev(QTextFormat *self) {
  delete self;
}

//  void QTextFormat::merge(const QTextFormat &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormat5mergeERKS_(
    QTextFormat *self,
    const QTextFormat *other) {
  self->merge(*other);
}

//  bool QTextFormat::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormat7isValidEv(const QTextFormat *self) {
  return self->isValid();
}

//  bool QTextFormat::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormat7isEmptyEv(const QTextFormat *self) {
  return self->isEmpty();
}

//  int QTextFormat::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextFormat4typeEv(const QTextFormat *self) {
  return self->type();
}

//  int QTextFormat::objectIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextFormat11objectIndexEv(const QTextFormat *self) {
  return self->objectIndex();
}

//  void QTextFormat::setObjectIndex(int object)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormat14setObjectIndexEi(
    QTextFormat *self,
    int object) {
  self->setObjectIndex(object);
}

//  QVariant QTextFormat::property(int propertyId) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QTextFormat8propertyEi(
    const QTextFormat *self,
    int propertyId) {
  return new QVariant(self->property(propertyId));
}

//  void QTextFormat::setProperty(int propertyId, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormat11setPropertyEiRK8QVariant(
    QTextFormat *self,
    int propertyId,
    const QVariant *value) {
  self->setProperty(propertyId, *value);
}

//  void QTextFormat::clearProperty(int propertyId)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormat13clearPropertyEi(
    QTextFormat *self,
    int propertyId) {
  self->clearProperty(propertyId);
}

//  bool QTextFormat::hasProperty(int propertyId) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormat11hasPropertyEi(
    const QTextFormat *self,
    int propertyId) {
  return self->hasProperty(propertyId);
}

//  bool QTextFormat::boolProperty(int propertyId) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormat12boolPropertyEi(
    const QTextFormat *self,
    int propertyId) {
  return self->boolProperty(propertyId);
}

//  int QTextFormat::intProperty(int propertyId) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextFormat11intPropertyEi(
    const QTextFormat *self,
    int propertyId) {
  return self->intProperty(propertyId);
}

//  qreal QTextFormat::doubleProperty(int propertyId) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QTextFormat14doublePropertyEi(
    const QTextFormat *self,
    int propertyId) {
  return self->doubleProperty(propertyId);
}

//  QString QTextFormat::stringProperty(int propertyId) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTextFormat14stringPropertyEi(
    const QTextFormat *self,
    int propertyId) {
  return new QString(self->stringProperty(propertyId));
}

//  QColor QTextFormat::colorProperty(int propertyId) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QTextFormat13colorPropertyEi(
    const QTextFormat *self,
    int propertyId) {
  return new QColor(self->colorProperty(propertyId));
}

//  QPen QTextFormat::penProperty(int propertyId) const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK11QTextFormat11penPropertyEi(
    const QTextFormat *self,
    int propertyId) {
  return new QPen(self->penProperty(propertyId));
}

//  QBrush QTextFormat::brushProperty(int propertyId) const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK11QTextFormat13brushPropertyEi(
    const QTextFormat *self,
    int propertyId) {
  return new QBrush(self->brushProperty(propertyId));
}

//  QTextLength QTextFormat::lengthProperty(int propertyId) const
extern "C" Q_DECL_EXPORT
QTextLength *ritual_ZNK11QTextFormat14lengthPropertyEi(
    const QTextFormat *self,
    int propertyId) {
  return new QTextLength(self->lengthProperty(propertyId));
}

//  QList<QTextLength> QTextFormat::lengthVectorProperty(int propertyId)
//      const
extern "C" Q_DECL_EXPORT
QList<QTextLength> *ritual_ZNK11QTextFormat20lengthVectorPropertyEi(
    const QTextFormat *self,
    int propertyId) {
  return new QList<QTextLength>(self->lengthVectorProperty(propertyId));
}

//  void QTextFormat::setProperty(int propertyId, const QList<QTextLength>
//      &lengths)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormat11setPropertyEiRK5QListI11QTextLengthE(
    QTextFormat *self,
    int propertyId,
    const QList<QTextLength> *lengths) {
  self->setProperty(propertyId, *lengths);
}

//  QMap<int, QVariant> QTextFormat::properties() const
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_ZNK11QTextFormat10propertiesEv(
    const QTextFormat *self) {
  return new QMap<int, QVariant>(self->properties());
}

//  int QTextFormat::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextFormat13propertyCountEv(const QTextFormat *self) {
  return self->propertyCount();
}

//  void QTextFormat::setObjectType(int type)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormat13setObjectTypeEi(QTextFormat *self, int type) {
  self->setObjectType(type);
}

//  int QTextFormat::objectType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextFormat10objectTypeEv(const QTextFormat *self) {
  return self->objectType();
}

//  bool QTextFormat::isCharFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormat12isCharFormatEv(const QTextFormat *self) {
  return self->isCharFormat();
}

//  bool QTextFormat::isBlockFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormat13isBlockFormatEv(const QTextFormat *self) {
  return self->isBlockFormat();
}

//  bool QTextFormat::isListFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormat12isListFormatEv(const QTextFormat *self) {
  return self->isListFormat();
}

//  bool QTextFormat::isFrameFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormat13isFrameFormatEv(const QTextFormat *self) {
  return self->isFrameFormat();
}

//  bool QTextFormat::isImageFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormat13isImageFormatEv(const QTextFormat *self) {
  return self->isImageFormat();
}

//  bool QTextFormat::isTableFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormat13isTableFormatEv(const QTextFormat *self) {
  return self->isTableFormat();
}

//  bool QTextFormat::isTableCellFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormat17isTableCellFormatEv(const QTextFormat *self) {
  return self->isTableCellFormat();
}

//  QTextBlockFormat QTextFormat::toBlockFormat() const
extern "C" Q_DECL_EXPORT
QTextBlockFormat *ritual_ZNK11QTextFormat13toBlockFormatEv(
    const QTextFormat *self) {
  return new QTextBlockFormat(self->toBlockFormat());
}

//  QTextCharFormat QTextFormat::toCharFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK11QTextFormat12toCharFormatEv(
    const QTextFormat *self) {
  return new QTextCharFormat(self->toCharFormat());
}

//  QTextListFormat QTextFormat::toListFormat() const
extern "C" Q_DECL_EXPORT
QTextListFormat *ritual_ZNK11QTextFormat12toListFormatEv(
    const QTextFormat *self) {
  return new QTextListFormat(self->toListFormat());
}

//  QTextTableFormat QTextFormat::toTableFormat() const
extern "C" Q_DECL_EXPORT
QTextTableFormat *ritual_ZNK11QTextFormat13toTableFormatEv(
    const QTextFormat *self) {
  return new QTextTableFormat(self->toTableFormat());
}

//  QTextFrameFormat QTextFormat::toFrameFormat() const
extern "C" Q_DECL_EXPORT
QTextFrameFormat *ritual_ZNK11QTextFormat13toFrameFormatEv(
    const QTextFormat *self) {
  return new QTextFrameFormat(self->toFrameFormat());
}

//  QTextImageFormat QTextFormat::toImageFormat() const
extern "C" Q_DECL_EXPORT
QTextImageFormat *ritual_ZNK11QTextFormat13toImageFormatEv(
    const QTextFormat *self) {
  return new QTextImageFormat(self->toImageFormat());
}

//  QTextTableCellFormat QTextFormat::toTableCellFormat() const
extern "C" Q_DECL_EXPORT
QTextTableCellFormat *ritual_ZNK11QTextFormat17toTableCellFormatEv(
    const QTextFormat *self) {
  return new QTextTableCellFormat(self->toTableCellFormat());
}

//  bool QTextFormat::operator==(const QTextFormat &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormateqERKS_(
    const QTextFormat *self,
    const QTextFormat *rhs) {
  return self->operator==(*rhs);
}

//  bool QTextFormat::operator!=(const QTextFormat &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextFormatneERKS_(
    const QTextFormat *self,
    const QTextFormat *rhs) {
  return self->operator!=(*rhs);
}

//  QVariant QTextFormat::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QTextFormatcv8QVariantEv(const QTextFormat *self) {
  return new QVariant(self->operator QVariant());
}

//  void QTextFormat::setLayoutDirection(Qt::LayoutDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormat18setLayoutDirectionEN2Qt15LayoutDirectionE(
    QTextFormat *self,
    Qt::LayoutDirection direction) {
  self->setLayoutDirection(direction);
}

//  Qt::LayoutDirection QTextFormat::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK11QTextFormat15layoutDirectionEv(
    const QTextFormat *self) {
  return self->layoutDirection();
}

//  void QTextFormat::setBackground(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormat13setBackgroundERK6QBrush(
    QTextFormat *self,
    const QBrush *brush) {
  self->setBackground(*brush);
}

//  QBrush QTextFormat::background() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK11QTextFormat10backgroundEv(const QTextFormat *self) {
  return new QBrush(self->background());
}

//  void QTextFormat::clearBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormat15clearBackgroundEv(QTextFormat *self) {
  self->clearBackground();
}

//  void QTextFormat::setForeground(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormat13setForegroundERK6QBrush(
    QTextFormat *self,
    const QBrush *brush) {
  self->setForeground(*brush);
}

//  QBrush QTextFormat::foreground() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK11QTextFormat10foregroundEv(const QTextFormat *self) {
  return new QBrush(self->foreground());
}

//  void QTextFormat::clearForeground()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextFormat15clearForegroundEv(QTextFormat *self) {
  self->clearForeground();
}

//  QList<QTextFormat>::QList()
extern "C" Q_DECL_EXPORT
QList<QTextFormat> *ritual_list_make_QTextFormat() {
  return new QList<QTextFormat>();
}

//  void QList<QTextFormat>::append(const QTextFormat &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QTextFormat(
    QList<QTextFormat> *self,
    const QTextFormat *element) {
  self->append(*element);
}

//  qsizetype QList<QTextFormat>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QTextFormat(const QList<QTextFormat> *self) {
  return self->size();
}

//  const QTextFormat &QList<QTextFormat>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_list_at_QTextFormat(
    const QList<QTextFormat> *self,
    long long index) {
  return new QTextFormat(self->at(index));
}

//  QList<QTextFormat>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QTextFormat(QList<QTextFormat> *self) {
  delete self;
}
