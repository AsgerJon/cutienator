//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qurl.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QQmlVMEMetaObject that Python can take functions over in. Every QQmlVMEMetaObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void * (*CuteQQmlVMEMetaObjectCall0)(const void *, QObject *, int *);
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void (*CuteQQmlVMEMetaObjectCall1)(const void *, QObject *, int *);
class CuteQQmlVMEMetaObject : public QQmlVMEMetaObject {
public:
  using QQmlVMEMetaObject::QQmlVMEMetaObject;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
    if (!std::strcmp(key, "_ZN22QDynamicMetaObjectData19toDynamicMetaObjectEP7QObject")) {
      taken[0] = call;
      return true;
    }
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
    if (!std::strcmp(key, "_ZN22QDynamicMetaObjectData15objectDestroyedEP7QObject")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
  //  QMetaObject *QQmlInterceptorMetaObject::toDynamicMetaObject(QObject
  //      *o)
  QMetaObject *toDynamicMetaObject(QObject *o) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlVMEMetaObjectCall0 call = reinterpret_cast<CuteQQmlVMEMetaObjectCall0>(taken[0]);
      void * given = call(this, o, &handled);
      if (handled) return static_cast<QMetaObject *>(given);
    }
    return QQmlInterceptorMetaObject::toDynamicMetaObject(o);
  }
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

  //  void QDynamicMetaObjectData::objectDestroyed(QObject *a0)
  void objectDestroyed(QObject *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlVMEMetaObjectCall1 call = reinterpret_cast<CuteQQmlVMEMetaObjectCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDynamicMetaObjectData::objectDestroyed(a0);
  }
};

//  QQmlVMEMetaObject::~QQmlVMEMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObjectD1Ev(QQmlVMEMetaObject *self) {
  delete self;
}

//  QV4::ReturnedValue QQmlVMEMetaObject::vmeMethod(int index) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK17QQmlVMEMetaObject9vmeMethodEi(
    const QQmlVMEMetaObject *self,
    int index) {
  return self->vmeMethod(index);
}

//  void QQmlVMEMetaObject::setVmeMethod(int index, const QV4::Value
//      &function)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject12setVmeMethodEiRKN3QV45ValueE(
    QQmlVMEMetaObject *self,
    int index,
    const QV4::Value *function) {
  self->setVmeMethod(index, *function);
}

//  QV4::ReturnedValue QQmlVMEMetaObject::vmeProperty(int index) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK17QQmlVMEMetaObject11vmePropertyEi(
    const QQmlVMEMetaObject *self,
    int index) {
  return self->vmeProperty(index);
}

//  void QQmlVMEMetaObject::setVMEProperty(int index, const QV4::Value &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject14setVMEPropertyEiRKN3QV45ValueE(
    QQmlVMEMetaObject *self,
    int index,
    const QV4::Value *v) {
  self->setVMEProperty(index, *v);
}

//  void QQmlVMEMetaObject::connectAliasSignal(int index, bool
//      indexInSignalRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject18connectAliasSignalEib(
    QQmlVMEMetaObject *self,
    int index,
    bool indexInSignalRange) {
  self->connectAliasSignal(index, indexInSignalRange);
}

//  QQmlVMEMetaObject *QQmlVMEMetaObject::get(QObject *o)
extern "C" Q_DECL_EXPORT
QQmlVMEMetaObject *ritual_ZN17QQmlVMEMetaObject3getEP7QObject(QObject *o) {
  return QQmlVMEMetaObject::get(o);
}

//  QQmlVMEMetaObject *QQmlVMEMetaObject::getForProperty(QObject *o, int
//      coreIndex)
extern "C" Q_DECL_EXPORT
QQmlVMEMetaObject *ritual_ZN17QQmlVMEMetaObject14getForPropertyEP7QObjecti(
    QObject *o,
    int coreIndex) {
  return QQmlVMEMetaObject::getForProperty(o, coreIndex);
}

//  QQmlVMEMetaObject *QQmlVMEMetaObject::getForMethod(QObject *o, int
//      coreIndex)
extern "C" Q_DECL_EXPORT
QQmlVMEMetaObject *ritual_ZN17QQmlVMEMetaObject12getForMethodEP7QObjecti(
    QObject *o,
    int coreIndex) {
  return QQmlVMEMetaObject::getForMethod(o, coreIndex);
}

//  QQmlVMEMetaObject *QQmlVMEMetaObject::getForSignal(QObject *o, int
//      coreIndex)
extern "C" Q_DECL_EXPORT
QQmlVMEMetaObject *ritual_ZN17QQmlVMEMetaObject12getForSignalEP7QObjecti(
    QObject *o,
    int coreIndex) {
  return QQmlVMEMetaObject::getForSignal(o, coreIndex);
}

//  int QQmlVMEMetaObject::propOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlVMEMetaObject10propOffsetEv(
    const QQmlVMEMetaObject *self) {
  return self->propOffset();
}

//  int QQmlVMEMetaObject::propCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlVMEMetaObject9propCountEv(
    const QQmlVMEMetaObject *self) {
  return self->propCount();
}

//  int QQmlVMEMetaObject::aliasOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlVMEMetaObject11aliasOffsetEv(
    const QQmlVMEMetaObject *self) {
  return self->aliasOffset();
}

//  int QQmlVMEMetaObject::aliasCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlVMEMetaObject10aliasCountEv(
    const QQmlVMEMetaObject *self) {
  return self->aliasCount();
}

//  int QQmlVMEMetaObject::signalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlVMEMetaObject12signalOffsetEv(
    const QQmlVMEMetaObject *self) {
  return self->signalOffset();
}

//  int QQmlVMEMetaObject::signalCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlVMEMetaObject11signalCountEv(
    const QQmlVMEMetaObject *self) {
  return self->signalCount();
}

//  int QQmlVMEMetaObject::methodOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlVMEMetaObject12methodOffsetEv(
    const QQmlVMEMetaObject *self) {
  return self->methodOffset();
}

//  int QQmlVMEMetaObject::methodCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlVMEMetaObject11methodCountEv(
    const QQmlVMEMetaObject *self) {
  return self->methodCount();
}

//  QV4::MemberData
//      *QQmlVMEMetaObject::propertyAndMethodStorageAsMemberData() const
extern "C" Q_DECL_EXPORT
QV4::MemberData *ritual_ZNK17QQmlVMEMetaObject36propertyAndMethodStorageAsMemberDataEv(
    const QQmlVMEMetaObject *self) {
  return self->propertyAndMethodStorageAsMemberData();
}

//  int QQmlVMEMetaObject::readPropertyAsInt(int id) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlVMEMetaObject17readPropertyAsIntEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return self->readPropertyAsInt(id);
}

//  bool QQmlVMEMetaObject::readPropertyAsBool(int id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlVMEMetaObject18readPropertyAsBoolEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return self->readPropertyAsBool(id);
}

//  double QQmlVMEMetaObject::readPropertyAsDouble(int id) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK17QQmlVMEMetaObject20readPropertyAsDoubleEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return self->readPropertyAsDouble(id);
}

//  QString QQmlVMEMetaObject::readPropertyAsString(int id) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQmlVMEMetaObject20readPropertyAsStringEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return new QString(self->readPropertyAsString(id));
}

//  QSizeF QQmlVMEMetaObject::readPropertyAsSizeF(int id) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK17QQmlVMEMetaObject19readPropertyAsSizeFEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return new QSizeF(self->readPropertyAsSizeF(id));
}

//  QPointF QQmlVMEMetaObject::readPropertyAsPointF(int id) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QQmlVMEMetaObject20readPropertyAsPointFEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return new QPointF(self->readPropertyAsPointF(id));
}

//  QUrl QQmlVMEMetaObject::readPropertyAsUrl(int id) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QQmlVMEMetaObject17readPropertyAsUrlEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return new QUrl(self->readPropertyAsUrl(id));
}

//  QDate QQmlVMEMetaObject::readPropertyAsDate(int id) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK17QQmlVMEMetaObject18readPropertyAsDateEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return new QDate(self->readPropertyAsDate(id));
}

//  QTime QQmlVMEMetaObject::readPropertyAsTime(int id) const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK17QQmlVMEMetaObject18readPropertyAsTimeEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return new QTime(self->readPropertyAsTime(id));
}

//  QDateTime QQmlVMEMetaObject::readPropertyAsDateTime(int id) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK17QQmlVMEMetaObject22readPropertyAsDateTimeEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return new QDateTime(self->readPropertyAsDateTime(id));
}

#if QT_CONFIG(regularexpression)
//  QRegularExpression QQmlVMEMetaObject::readPropertyAsRegularExpression(int
//      id) const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK17QQmlVMEMetaObject31readPropertyAsRegularExpressionEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return new QRegularExpression(self->readPropertyAsRegularExpression(id));
}
#endif  // QT_CONFIG(regularexpression)

//  QRectF QQmlVMEMetaObject::readPropertyAsRectF(int id) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQmlVMEMetaObject19readPropertyAsRectFEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return new QRectF(self->readPropertyAsRectF(id));
}

//  QObject *QQmlVMEMetaObject::readPropertyAsQObject(int id) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QQmlVMEMetaObject21readPropertyAsQObjectEi(
    const QQmlVMEMetaObject *self,
    int id) {
  return self->readPropertyAsQObject(id);
}

//  void QQmlVMEMetaObject::initPropertyAsList(int id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QQmlVMEMetaObject18initPropertyAsListEi(
    const QQmlVMEMetaObject *self,
    int id) {
  self->initPropertyAsList(id);
}

//  void QQmlVMEMetaObject::writeProperty(int id, int v)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject13writePropertyEii(
    QQmlVMEMetaObject *self,
    int id,
    int v) {
  self->writeProperty(id, v);
}

//  void QQmlVMEMetaObject::writeProperty(int id, bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject13writePropertyEib(
    QQmlVMEMetaObject *self,
    int id,
    bool v) {
  self->writeProperty(id, v);
}

//  void QQmlVMEMetaObject::writeProperty(int id, double v)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject13writePropertyEid(
    QQmlVMEMetaObject *self,
    int id,
    double v) {
  self->writeProperty(id, v);
}

//  void QQmlVMEMetaObject::writeProperty(int id, const QString &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject13writePropertyEiRK7QString(
    QQmlVMEMetaObject *self,
    int id,
    const QString *v) {
  self->writeProperty(id, *v);
}

//  void QQmlVMEMetaObject::writeProperty(int id, QObject *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject13writePropertyEiP7QObject(
    QQmlVMEMetaObject *self,
    int id,
    QObject *v) {
  self->writeProperty(id, v);
}

//  void QQmlVMEMetaObject::ensureQObjectWrapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject20ensureQObjectWrapperEv(
    QQmlVMEMetaObject *self) {
  self->ensureQObjectWrapper();
}

//  void QQmlVMEMetaObject::mark(QV4::MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject4markEPN3QV49MarkStackE(
    QQmlVMEMetaObject *self,
    QV4::MarkStack *markStack) {
  self->mark(markStack);
}

//  void QQmlVMEMetaObject::connectAlias(const QV4::CompiledData::Object
//      *compiledObject, int aliasId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject12connectAliasEPKN3QV412CompiledData6ObjectEi(
    QQmlVMEMetaObject *self,
    const QV4::CompiledData::Object *compiledObject,
    int aliasId) {
  self->connectAlias(compiledObject, aliasId);
}

//  QV4::ReturnedValue QQmlVMEMetaObject::method(int a0) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK17QQmlVMEMetaObject6methodEi(
    const QQmlVMEMetaObject *self,
    int a0) {
  return self->method(a0);
}

//  QV4::ReturnedValue QQmlVMEMetaObject::readVarProperty(int a0) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK17QQmlVMEMetaObject15readVarPropertyEi(
    const QQmlVMEMetaObject *self,
    int a0) {
  return self->readVarProperty(a0);
}

//  void QQmlVMEMetaObject::writeVarProperty(int a0, const QV4::Value &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject16writeVarPropertyEiRKN3QV45ValueE(
    QQmlVMEMetaObject *self,
    int a0,
    const QV4::Value *a1) {
  self->writeVarProperty(a0, *a1);
}

//  QVariant QQmlVMEMetaObject::readPropertyAsVariant(int a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QQmlVMEMetaObject21readPropertyAsVariantEi(
    const QQmlVMEMetaObject *self,
    int a0) {
  return new QVariant(self->readPropertyAsVariant(a0));
}

//  QQmlVMEMetaObject *QQmlVMEMetaObject::parentVMEMetaObject() const
extern "C" Q_DECL_EXPORT
QQmlVMEMetaObject *ritual_ZNK17QQmlVMEMetaObject19parentVMEMetaObjectEv(
    const QQmlVMEMetaObject *self) {
  return self->parentVMEMetaObject();
}

//  void QQmlVMEMetaObject::setParentVMEMetaObject(QQmlVMEMetaObject
//      *newParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject22setParentVMEMetaObjectEPS_(
    QQmlVMEMetaObject *self,
    QQmlVMEMetaObject *newParent) {
  self->setParentVMEMetaObject(newParent);
}

//  QQmlVMEVariantQObjectPtr
//      *QQmlVMEMetaObject::getQObjectGuardForProperty(int a0) const
extern "C" Q_DECL_EXPORT
QQmlVMEVariantQObjectPtr *ritual_ZNK17QQmlVMEMetaObject26getQObjectGuardForPropertyEi(
    const QQmlVMEMetaObject *self,
    int a0) {
  return self->getQObjectGuardForProperty(a0);
}

//  QV4::ExecutionEngine *QQmlVMEMetaObject::engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK17QQmlVMEMetaObject6engineEv(
    const QQmlVMEMetaObject *self) {
  return self->engine();
}

//  int QQmlVMEMetaObject::qmlObjectId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlVMEMetaObject11qmlObjectIdEv(
    const QQmlVMEMetaObject *self) {
  return self->qmlObjectId();
}

//  const QV4::CompiledData::Object *QQmlVMEMetaObject::findCompiledObject()
//      const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Object *ritual_ZNK17QQmlVMEMetaObject18findCompiledObjectEv(
    const QQmlVMEMetaObject *self) {
  return self->findCompiledObject();
}

//  void QQmlVMEMetaObject::writeKnownVarProperty(int id, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlVMEMetaObject21writeKnownVarPropertyEiRK8QVariant(
    QQmlVMEMetaObject *self,
    int id,
    const QVariant *value) {
  self->writeKnownVarProperty(id, *value);
}

//  a Python function taken by a CuteQQmlVMEMetaObject, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlVMEMetaObject(
    QQmlVMEMetaObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlVMEMetaObject *>(self)->take(key, call);
}
