//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qvariant.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qvariant.h>
#include <QtCore/qchar.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbitarray.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qlocale.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/quuid.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qline.h>
#include <QtCore/qrect.h>
#include <QtCore/qeasingcurve.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qcompare.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QVariant::QVariant()
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1Ev() {
  return new QVariant();
}

//  QVariant::~QVariant()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QVariantD1Ev(QVariant *self) {
  delete self;
}

//  QVariant::QVariant(const QVariant &other)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERKS_(const QVariant *other) {
  return new QVariant(*other);
}

//  QVariant::QVariant(int i)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1Ei(int i) {
  return new QVariant(i);
}

//  QVariant::QVariant(uint ui)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1Ej(uint ui) {
  return new QVariant(ui);
}

//  QVariant::QVariant(qlonglong ll)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1Ex(qlonglong ll) {
  return new QVariant(ll);
}

//  QVariant::QVariant(qulonglong ull)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1Ey(qulonglong ull) {
  return new QVariant(ull);
}

//  QVariant::QVariant(bool b)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1Eb(bool b) {
  return new QVariant(b);
}

//  QVariant::QVariant(double d)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1Ed(double d) {
  return new QVariant(d);
}

//  QVariant::QVariant(float f)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1Ef(float f) {
  return new QVariant(f);
}

//  QVariant::QVariant(QChar qchar)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E5QChar(const QChar *qchar) {
  return new QVariant(*qchar);
}

//  QVariant::QVariant(QDate date)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E5QDate(const QDate *date) {
  return new QVariant(*date);
}

//  QVariant::QVariant(QTime time)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E5QTime(const QTime *time) {
  return new QVariant(*time);
}

//  QVariant::QVariant(const QBitArray &bitarray)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK9QBitArray(const QBitArray *bitarray) {
  return new QVariant(*bitarray);
}

//  QVariant::QVariant(const QByteArray &bytearray)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK10QByteArray(const QByteArray *bytearray) {
  return new QVariant(*bytearray);
}

//  QVariant::QVariant(const QDateTime &datetime)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK9QDateTime(const QDateTime *datetime) {
  return new QVariant(*datetime);
}

//  QVariant::QVariant(const QHash<QString, QVariant> &hash)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK5QHashI7QStringS_E(
    const QHash<QString, QVariant> *hash) {
  return new QVariant(*hash);
}

//  QVariant::QVariant(const QJsonArray &jsonArray)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK10QJsonArray(const QJsonArray *jsonArray) {
  return new QVariant(*jsonArray);
}

//  QVariant::QVariant(const QJsonObject &jsonObject)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK11QJsonObject(
    const QJsonObject *jsonObject) {
  return new QVariant(*jsonObject);
}

//  QVariant::QVariant(const QList<QVariant> &list)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK5QListIS_E(const QList<QVariant> *list) {
  return new QVariant(*list);
}

//  QVariant::QVariant(const QLocale &locale)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK7QLocale(const QLocale *locale) {
  return new QVariant(*locale);
}

//  QVariant::QVariant(const QMap<QString, QVariant> &map)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK4QMapI7QStringS_E(
    const QMap<QString, QVariant> *map) {
  return new QVariant(*map);
}

//  QVariant::QVariant(const QRegularExpression &re)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK18QRegularExpression(
    const QRegularExpression *re) {
  return new QVariant(*re);
}

//  QVariant::QVariant(const QString &string)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK7QString(const QString *string) {
  return new QVariant(*string);
}

//  QVariant::QVariant(const QStringList &stringlist)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK5QListI7QStringE(
    const QList<QString> *stringlist) {
  return new QVariant(*stringlist);
}

//  QVariant::QVariant(const QUrl &url)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK4QUrl(const QUrl *url) {
  return new QVariant(*url);
}

//  QVariant::QVariant(const QJsonValue &jsonValue)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK10QJsonValue(const QJsonValue *jsonValue) {
  return new QVariant(*jsonValue);
}

//  QVariant::QVariant(const QModelIndex &modelIndex)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK11QModelIndex(
    const QModelIndex *modelIndex) {
  return new QVariant(*modelIndex);
}

//  QVariant::QVariant(QUuid uuid)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E5QUuid(const QUuid *uuid) {
  return new QVariant(*uuid);
}

//  QVariant::QVariant(QSize size)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E5QSize(const QSize *size) {
  return new QVariant(*size);
}

//  QVariant::QVariant(QSizeF size)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E6QSizeF(const QSizeF *size) {
  return new QVariant(*size);
}

//  QVariant::QVariant(QPoint pt)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E6QPoint(const QPoint *pt) {
  return new QVariant(*pt);
}

//  QVariant::QVariant(QPointF pt)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E7QPointF(const QPointF *pt) {
  return new QVariant(*pt);
}

//  QVariant::QVariant(QLine line)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E5QLine(const QLine *line) {
  return new QVariant(*line);
}

//  QVariant::QVariant(QLineF line)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E6QLineF(const QLineF *line) {
  return new QVariant(*line);
}

//  QVariant::QVariant(QRect rect)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E5QRect(const QRect *rect) {
  return new QVariant(*rect);
}

//  QVariant::QVariant(QRectF rect)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E6QRectF(const QRectF *rect) {
  return new QVariant(*rect);
}

//  QVariant::QVariant(const QEasingCurve &easing)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK12QEasingCurve(const QEasingCurve *easing) {
  return new QVariant(*easing);
}

//  QVariant::QVariant(const QJsonDocument &jsonDocument)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK13QJsonDocument(
    const QJsonDocument *jsonDocument) {
  return new QVariant(*jsonDocument);
}

//  QVariant::QVariant(const QPersistentModelIndex &modelIndex)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ERK21QPersistentModelIndex(
    const QPersistentModelIndex *modelIndex) {
  return new QVariant(*modelIndex);
}

//  QVariant::QVariant(const char *str)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1EPKc(const char *str) {
  return new QVariant(str);
}

//  QVariant::QVariant(QLatin1StringView string)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1E13QLatin1String(const QLatin1String *string) {
  return new QVariant(*string);
}

//  int QVariant::userType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QVariant8userTypeEv(const QVariant *self) {
  return self->userType();
}

//  int QVariant::typeId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QVariant6typeIdEv(const QVariant *self) {
  return self->typeId();
}

//  const char *QVariant::typeName() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK8QVariant8typeNameEv(const QVariant *self) {
  return self->typeName();
}

//  QMetaType QVariant::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK8QVariant8metaTypeEv(const QVariant *self) {
  return new QMetaType(self->metaType());
}

//  bool QVariant::canConvert(QMetaType targetType) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QVariant10canConvertE9QMetaType(
    const QVariant *self,
    const QMetaType *targetType) {
  return self->canConvert(*targetType);
}

//  bool QVariant::convert(QMetaType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QVariant7convertE9QMetaType(
    QVariant *self,
    const QMetaType *type) {
  return self->convert(*type);
}

//  bool QVariant::canView(QMetaType targetType) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QVariant7canViewE9QMetaType(
    const QVariant *self,
    const QMetaType *targetType) {
  return self->canView(*targetType);
}

//  bool QVariant::canConvert(int targetTypeId) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QVariant10canConvertEi(
    const QVariant *self,
    int targetTypeId) {
  return self->canConvert(targetTypeId);
}

//  bool QVariant::convert(int targetTypeId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QVariant7convertEi(QVariant *self, int targetTypeId) {
  return self->convert(targetTypeId);
}

//  bool QVariant::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QVariant7isValidEv(const QVariant *self) {
  return self->isValid();
}

//  bool QVariant::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QVariant6isNullEv(const QVariant *self) {
  return self->isNull();
}

//  void QVariant::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QVariant5clearEv(QVariant *self) {
  self->clear();
}

//  void QVariant::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QVariant6detachEv(QVariant *self) {
  self->detach();
}

//  bool QVariant::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QVariant10isDetachedEv(const QVariant *self) {
  return self->isDetached();
}

//  int QVariant::toInt(bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QVariant5toIntEPb(const QVariant *self, bool *ok) {
  return self->toInt(ok);
}

//  uint QVariant::toUInt(bool *ok) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK8QVariant6toUIntEPb(const QVariant *self, bool *ok) {
  return self->toUInt(ok);
}

//  qlonglong QVariant::toLongLong(bool *ok) const
extern "C" Q_DECL_EXPORT
qlonglong ritual_ZNK8QVariant10toLongLongEPb(
    const QVariant *self,
    bool *ok) {
  return self->toLongLong(ok);
}

//  qulonglong QVariant::toULongLong(bool *ok) const
extern "C" Q_DECL_EXPORT
qulonglong ritual_ZNK8QVariant11toULongLongEPb(
    const QVariant *self,
    bool *ok) {
  return self->toULongLong(ok);
}

//  bool QVariant::toBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QVariant6toBoolEv(const QVariant *self) {
  return self->toBool();
}

//  double QVariant::toDouble(bool *ok) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK8QVariant8toDoubleEPb(const QVariant *self, bool *ok) {
  return self->toDouble(ok);
}

//  float QVariant::toFloat(bool *ok) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8QVariant7toFloatEPb(const QVariant *self, bool *ok) {
  return self->toFloat(ok);
}

//  qreal QVariant::toReal(bool *ok) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QVariant6toRealEPb(const QVariant *self, bool *ok) {
  return self->toReal(ok);
}

//  QByteArray QVariant::toByteArray() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK8QVariant11toByteArrayEv(const QVariant *self) {
  return new QByteArray(self->toByteArray());
}

//  QBitArray QVariant::toBitArray() const
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZNK8QVariant10toBitArrayEv(const QVariant *self) {
  return new QBitArray(self->toBitArray());
}

//  QString QVariant::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QVariant8toStringEv(const QVariant *self) {
  return new QString(self->toString());
}

//  QStringList QVariant::toStringList() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8QVariant12toStringListEv(const QVariant *self) {
  return new QList<QString>(self->toStringList());
}

//  QChar QVariant::toChar() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK8QVariant6toCharEv(const QVariant *self) {
  return new QChar(self->toChar());
}

//  QDate QVariant::toDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK8QVariant6toDateEv(const QVariant *self) {
  return new QDate(self->toDate());
}

//  QTime QVariant::toTime() const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK8QVariant6toTimeEv(const QVariant *self) {
  return new QTime(self->toTime());
}

//  QDateTime QVariant::toDateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK8QVariant10toDateTimeEv(const QVariant *self) {
  return new QDateTime(self->toDateTime());
}

//  QList<QVariant> QVariant::toList() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK8QVariant6toListEv(const QVariant *self) {
  return new QList<QVariant>(self->toList());
}

//  QMap<QString, QVariant> QVariant::toMap() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK8QVariant5toMapEv(const QVariant *self) {
  return new QMap<QString, QVariant>(self->toMap());
}

//  QHash<QString, QVariant> QVariant::toHash() const
extern "C" Q_DECL_EXPORT
QHash<QString, QVariant> *ritual_ZNK8QVariant6toHashEv(
    const QVariant *self) {
  return new QHash<QString, QVariant>(self->toHash());
}

//  QPoint QVariant::toPoint() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK8QVariant7toPointEv(const QVariant *self) {
  return new QPoint(self->toPoint());
}

//  QPointF QVariant::toPointF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8QVariant8toPointFEv(const QVariant *self) {
  return new QPointF(self->toPointF());
}

//  QRect QVariant::toRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8QVariant6toRectEv(const QVariant *self) {
  return new QRect(self->toRect());
}

//  QSize QVariant::toSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QVariant6toSizeEv(const QVariant *self) {
  return new QSize(self->toSize());
}

//  QSizeF QVariant::toSizeF() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK8QVariant7toSizeFEv(const QVariant *self) {
  return new QSizeF(self->toSizeF());
}

//  QLine QVariant::toLine() const
extern "C" Q_DECL_EXPORT
QLine *ritual_ZNK8QVariant6toLineEv(const QVariant *self) {
  return new QLine(self->toLine());
}

//  QLineF QVariant::toLineF() const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK8QVariant7toLineFEv(const QVariant *self) {
  return new QLineF(self->toLineF());
}

//  QRectF QVariant::toRectF() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QVariant7toRectFEv(const QVariant *self) {
  return new QRectF(self->toRectF());
}

//  QLocale QVariant::toLocale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK8QVariant8toLocaleEv(const QVariant *self) {
  return new QLocale(self->toLocale());
}

//  QRegularExpression QVariant::toRegularExpression() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK8QVariant19toRegularExpressionEv(
    const QVariant *self) {
  return new QRegularExpression(self->toRegularExpression());
}

//  QEasingCurve QVariant::toEasingCurve() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK8QVariant13toEasingCurveEv(const QVariant *self) {
  return new QEasingCurve(self->toEasingCurve());
}

//  QUuid QVariant::toUuid() const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK8QVariant6toUuidEv(const QVariant *self) {
  return new QUuid(self->toUuid());
}

//  QUrl QVariant::toUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK8QVariant5toUrlEv(const QVariant *self) {
  return new QUrl(self->toUrl());
}

//  QJsonValue QVariant::toJsonValue() const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK8QVariant11toJsonValueEv(const QVariant *self) {
  return new QJsonValue(self->toJsonValue());
}

//  QJsonObject QVariant::toJsonObject() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK8QVariant12toJsonObjectEv(const QVariant *self) {
  return new QJsonObject(self->toJsonObject());
}

//  QJsonArray QVariant::toJsonArray() const
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZNK8QVariant11toJsonArrayEv(const QVariant *self) {
  return new QJsonArray(self->toJsonArray());
}

//  QJsonDocument QVariant::toJsonDocument() const
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZNK8QVariant14toJsonDocumentEv(const QVariant *self) {
  return new QJsonDocument(self->toJsonDocument());
}

//  QModelIndex QVariant::toModelIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK8QVariant12toModelIndexEv(const QVariant *self) {
  return new QModelIndex(self->toModelIndex());
}

//  QPersistentModelIndex QVariant::toPersistentModelIndex() const
extern "C" Q_DECL_EXPORT
QPersistentModelIndex *ritual_ZNK8QVariant22toPersistentModelIndexEv(
    const QVariant *self) {
  return new QPersistentModelIndex(self->toPersistentModelIndex());
}

//  QVariant::QVariant(Type type)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8QVariantC1ENS_4TypeE(QVariant::Type type) {
  return new QVariant(type);
}

//  Type QVariant::type() const
extern "C" Q_DECL_EXPORT
QVariant::Type ritual_ZNK8QVariant4typeEv(const QVariant *self) {
  return self->type();
}

//  const char *QVariant::typeToName(int typeId)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN8QVariant10typeToNameEi(int typeId) {
  return QVariant::typeToName(typeId);
}

//  Type QVariant::nameToType(const char *name)
extern "C" Q_DECL_EXPORT
QVariant::Type ritual_ZN8QVariant10nameToTypeEPKc(const char *name) {
  return QVariant::nameToType(name);
}

//  void QVariant::setValue(const QVariant &avalue)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QVariant8setValueERKS_(
    QVariant *self,
    const QVariant *avalue) {
  self->setValue(*avalue);
}

//  QPartialOrdering QVariant::compare(const QVariant &lhs, const QVariant
//      &rhs)
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZN8QVariant7compareERKS_S1_(
    const QVariant *lhs,
    const QVariant *rhs) {
  return new QPartialOrdering(QVariant::compare(*lhs, *rhs));
}

//  bool operator==(const QVariant &lhs, const QVariant &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8QVariantS1_(const QVariant *lhs, const QVariant *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QVariant &lhs, const QVariant &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8QVariantS1_(const QVariant *lhs, const QVariant *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QDebug QVariant::qdebugHelper(QDebug a0) const
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZNK8QVariant12qdebugHelperE6QDebug(
    const QVariant *self,
    const QDebug *a0) {
  return new QDebug(self->qdebugHelper(*a0));
}

//  bool QVariant::equals(const QVariant &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QVariant6equalsERKS_(
    const QVariant *self,
    const QVariant *other) {
  return self->equals(*other);
}

//  QList<QVariant>::QList()
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_list_make_QVariant() {
  return new QList<QVariant>();
}

//  void QList<QVariant>::append(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QVariant(
    QList<QVariant> *self,
    const QVariant *element) {
  self->append(*element);
}

//  qsizetype QList<QVariant>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QVariant(const QList<QVariant> *self) {
  return self->size();
}

//  const QVariant &QList<QVariant>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_list_at_QVariant(
    const QList<QVariant> *self,
    long long index) {
  return new QVariant(self->at(index));
}

//  QList<QVariant>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QVariant(QList<QVariant> *self) {
  delete self;
}

//  QMap<QString, QVariant>: QMap<QString, QVariant>()
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_map_make_QMap_QString_QVariant() {
  return new QMap<QString, QVariant>();
}

//  QMap<QString, QVariant>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QMap_QString_QVariant(
    QMap<QString, QVariant> *self,
    const QString *key,
    const QVariant *value) {
  self->insert(*key, *value);
}

//  QMap<QString, QVariant>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QMap_QString_QVariant(
    const QMap<QString, QVariant> *self) {
  return self->size();
}

//  QMap<QString, QVariant>: the key at a place
extern "C" Q_DECL_EXPORT
QString *ritual_map_key_QMap_QString_QVariant(
    const QMap<QString, QVariant> *self,
    long long index) {
  return new QString(*std::next(self->keyBegin(), index));
}

//  QMap<QString, QVariant>: the value at a place
extern "C" Q_DECL_EXPORT
QVariant *ritual_map_value_QMap_QString_QVariant(
    const QMap<QString, QVariant> *self,
    long long index) {
  return new QVariant(*std::next(self->constBegin(), index));
}

//  QMap<QString, QVariant>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QMap_QString_QVariant(
    const QMap<QString, QVariant> *self,
    const QString *key) {
  return self->contains(*key);
}

//  QMap<QString, QVariant>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_map_get_QMap_QString_QVariant(
    const QMap<QString, QVariant> *self,
    const QString *key) {
  return new QVariant(self->value(*key));
}

//  QMap<QString, QVariant>: ~QMap()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QMap_QString_QVariant(QMap<QString, QVariant> *self) {
  delete self;
}

//  QHash<QString, QVariant>: QHash<QString, QVariant>()
extern "C" Q_DECL_EXPORT
QHash<QString, QVariant> *ritual_map_make_QHash_QString_QVariant() {
  return new QHash<QString, QVariant>();
}

//  QHash<QString, QVariant>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QHash_QString_QVariant(
    QHash<QString, QVariant> *self,
    const QString *key,
    const QVariant *value) {
  self->insert(*key, *value);
}

//  QHash<QString, QVariant>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QHash_QString_QVariant(
    const QHash<QString, QVariant> *self) {
  return self->size();
}

//  QHash<QString, QVariant>: the key at a place
extern "C" Q_DECL_EXPORT
QString *ritual_map_key_QHash_QString_QVariant(
    const QHash<QString, QVariant> *self,
    long long index) {
  return new QString(*std::next(self->keyBegin(), index));
}

//  QHash<QString, QVariant>: the value at a place
extern "C" Q_DECL_EXPORT
QVariant *ritual_map_value_QHash_QString_QVariant(
    const QHash<QString, QVariant> *self,
    long long index) {
  return new QVariant(*std::next(self->constBegin(), index));
}

//  QHash<QString, QVariant>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QHash_QString_QVariant(
    const QHash<QString, QVariant> *self,
    const QString *key) {
  return self->contains(*key);
}

//  QHash<QString, QVariant>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_map_get_QHash_QString_QVariant(
    const QHash<QString, QVariant> *self,
    const QString *key) {
  return new QVariant(self->value(*key));
}

//  QHash<QString, QVariant>: ~QHash()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QHash_QString_QVariant(QHash<QString, QVariant> *self) {
  delete self;
}

//  QMap<int, QVariant>: QMap<int, QVariant>()
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_map_make_QMap_int_QVariant() {
  return new QMap<int, QVariant>();
}

//  QMap<int, QVariant>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QMap_int_QVariant(
    QMap<int, QVariant> *self,
    int key,
    const QVariant *value) {
  self->insert(key, *value);
}

//  QMap<int, QVariant>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QMap_int_QVariant(
    const QMap<int, QVariant> *self) {
  return self->size();
}

//  QMap<int, QVariant>: the key at a place
extern "C" Q_DECL_EXPORT
int ritual_map_key_QMap_int_QVariant(
    const QMap<int, QVariant> *self,
    long long index) {
  return *std::next(self->keyBegin(), index);
}

//  QMap<int, QVariant>: the value at a place
extern "C" Q_DECL_EXPORT
QVariant *ritual_map_value_QMap_int_QVariant(
    const QMap<int, QVariant> *self,
    long long index) {
  return new QVariant(*std::next(self->constBegin(), index));
}

//  QMap<int, QVariant>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QMap_int_QVariant(
    const QMap<int, QVariant> *self,
    int key) {
  return self->contains(key);
}

//  QMap<int, QVariant>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_map_get_QMap_int_QVariant(
    const QMap<int, QVariant> *self,
    int key) {
  return new QVariant(self->value(key));
}

//  QMap<int, QVariant>: ~QMap()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QMap_int_QVariant(QMap<int, QVariant> *self) {
  delete self;
}
