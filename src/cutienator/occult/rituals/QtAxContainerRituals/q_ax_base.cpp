//  Written by hand on 2026-11-25 from QtAxContainer/qaxbase.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again. ActiveQt
//  is built for Windows alone, as a static library, so every function of it
//  is compiled into ours. The COM interfaces of Windows, as 'IUnknown', and
//  a 'void *' are passed as addresses; a 'long' and a 'ulong' as the numbers
//  Windows has. Its constructor is not written: it is protected and makes a
//  bare QAxBase, without the data QAxObject and QAxWidget give it through
//  'axBaseInit', and Qt's destructor then uses data that is not there;
//  Python makes a QAxObject or a QAxWidget instead. Not written:
//  'propertyBag', 'setPropertyBag', 'verbs', 'argumentsToList',
//  'dynamicCallHelper' and the 'dynamicCall' and 'querySubObject' taking a
//  'QList<QVariant> &', which take or give a list or a map; the friends
//  'operator>>' and 'operator<<', which take a 'QDataStream &'; the
//  templates of 'qobject_cast'; and 'qax_generateDocumentation', of no
//  class. Its Cute class takes no 'propertyWritable' or
//  'setPropertyWritable' over: they take a 'const char *', which is handed
//  to no Python function.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/qaxbase.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/quuid.h>
#include <cstring>

//  Only a class built on QAxBase may call these functions of it. This one
//  is, and makes them free for the rituals to call.
struct OwnQAxBase : QAxBase {
  using QAxBase::initialize;
};

//  A QAxBase that Python can take functions over in. Every QAxBase Python
//  makes is one. Each function below asks the Python function handed over
//  for it, and runs Qt's own without one.
typedef bool (*CuteQAxBaseCall0)(const void *, IUnknown **, int *);
class CuteQAxBase : public QAxBase {
public:
  using QAxBase::QAxBase;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QAxBase10initializeEPP8IUnknown")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QAxBase::initialize(IUnknown **ptr)
  bool initialize(IUnknown **ptr) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAxBaseCall0 call = reinterpret_cast<CuteQAxBaseCall0>(taken[0]);
      bool given = call(this, ptr, &handled);
      if (handled) return given;
    }
    return QAxBase::initialize(ptr);
  }
};

//  QAxBase::~QAxBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAxBaseD1Ev(QAxBase *self) {
  delete self;
}

//  QString QAxBase::control() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QAxBase7controlEv(const QAxBase *self) {
  return new QString(self->control());
}

//  long QAxBase::queryInterface(const QUuid &a0, void **a1) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK7QAxBase14queryInterfaceERK5QUuidPPv(
    const QAxBase *self,
    const QUuid *a0,
    void **a1) {
  return self->queryInterface(*a0, a1);
}

//  QVariant QAxBase::dynamicCall(const char *name, const QVariant &v1, const
//      QVariant &v2, const QVariant &v3, const QVariant &v4, const QVariant
//      &v5, const QVariant &v6, const QVariant &v7, const QVariant &v8)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN7QAxBase11dynamicCallEPKcRK8QVariantS4_S4_S4_S4_S4_S4_S4_(
    QAxBase *self,
    const char *name,
    const QVariant *v1,
    const QVariant *v2,
    const QVariant *v3,
    const QVariant *v4,
    const QVariant *v5,
    const QVariant *v6,
    const QVariant *v7,
    const QVariant *v8) {
  return new QVariant(
      self->dynamicCall(
          name,
          *v1,
          *v2,
          *v3,
          *v4,
          *v5,
          *v6,
          *v7,
          *v8));
}

//  QAxObject *QAxBase::querySubObject(const char *name, const QVariant &v1,
//      const QVariant &v2, const QVariant &v3, const QVariant &v4, const
//      QVariant &v5, const QVariant &v6, const QVariant &v7, const QVariant
//      &v8)
extern "C" Q_DECL_EXPORT
QAxObject *ritual_ZN7QAxBase14querySubObjectEPKcRK8QVariantS4_S4_S4_S4_S4_S4_S4_(
    QAxBase *self,
    const char *name,
    const QVariant *v1,
    const QVariant *v2,
    const QVariant *v3,
    const QVariant *v4,
    const QVariant *v5,
    const QVariant *v6,
    const QVariant *v7,
    const QVariant *v8) {
  return self->querySubObject(name, *v1, *v2, *v3, *v4, *v5, *v6, *v7, *v8);
}

//  const QMetaObject *QAxBase::axBaseMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QAxBase16axBaseMetaObjectEv(
    const QAxBase *self) {
  return self->axBaseMetaObject();
}

//  const char *QAxBase::className() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK7QAxBase9classNameEv(const QAxBase *self) {
  return self->className();
}

//  QObject *QAxBase::qObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK7QAxBase7qObjectEv(const QAxBase *self) {
  return self->qObject();
}

//  QString QAxBase::generateDocumentation()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QAxBase21generateDocumentationEv(QAxBase *self) {
  return new QString(self->generateDocumentation());
}

//  bool QAxBase::propertyWritable(const char *a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QAxBase16propertyWritableEPKc(
    const QAxBase *self,
    const char *a0) {
  return self->propertyWritable(a0);
}

//  void QAxBase::setPropertyWritable(const char *a0, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAxBase19setPropertyWritableEPKcb(
    QAxBase *self,
    const char *a0,
    bool a1) {
  self->setPropertyWritable(a0, a1);
}

//  bool QAxBase::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QAxBase6isNullEv(const QAxBase *self) {
  return self->isNull();
}

//  QVariant QAxBase::asVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QAxBase9asVariantEv(const QAxBase *self) {
  return new QVariant(self->asVariant());
}

//  void QAxBase::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAxBase5clearEv(QAxBase *self) {
  self->clear();
}

//  bool QAxBase::setControl(const QString &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QAxBase10setControlERK7QString(
    QAxBase *self,
    const QString *a0) {
  return self->setControl(*a0);
}

//  void QAxBase::disableMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAxBase17disableMetaObjectEv(QAxBase *self) {
  self->disableMetaObject();
}

//  void QAxBase::disableClassInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAxBase16disableClassInfoEv(QAxBase *self) {
  self->disableClassInfo();
}

//  void QAxBase::disableEventSink()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAxBase16disableEventSinkEv(QAxBase *self) {
  self->disableEventSink();
}

//  ulong QAxBase::classContext() const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK7QAxBase12classContextEv(const QAxBase *self) {
  return self->classContext();
}

//  void QAxBase::setClassContext(ulong classContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAxBase15setClassContextEm(
    QAxBase *self,
    ulong classContext) {
  self->setClassContext(classContext);
}

//  bool QAxBase::initialize(IUnknown **ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QAxBase10initializeEPP8IUnknown(
    QAxBase *self,
    IUnknown **ptr) {
  return self->initialize(ptr);
}

//  bool QAxBase::initializeRemote(IUnknown **ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QAxBase16initializeRemoteEPP8IUnknown(
    QAxBase *self,
    IUnknown **ptr) {
  return self->initializeRemote(ptr);
}

//  bool QAxBase::initializeLicensed(IUnknown **ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QAxBase18initializeLicensedEPP8IUnknown(
    QAxBase *self,
    IUnknown **ptr) {
  return self->initializeLicensed(ptr);
}

//  bool QAxBase::initializeActive(IUnknown **ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QAxBase16initializeActiveEPP8IUnknown(
    QAxBase *self,
    IUnknown **ptr) {
  return self->initializeActive(ptr);
}

//  bool QAxBase::initializeFromFile(IUnknown **ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QAxBase18initializeFromFileEPP8IUnknown(
    QAxBase *self,
    IUnknown **ptr) {
  return self->initializeFromFile(ptr);
}

//  void QAxBase::internalRelease()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAxBase15internalReleaseEv(QAxBase *self) {
  self->internalRelease();
}

//  void QAxBase::initializeFrom(QAxBase *that)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAxBase14initializeFromEPS_(QAxBase *self, QAxBase *that) {
  self->initializeFrom(that);
}

//  void QAxBase::connectNotify()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAxBase13connectNotifyEv(QAxBase *self) {
  self->connectNotify();
}

//  long QAxBase::indexOfVerb(const QString &verb) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK7QAxBase11indexOfVerbERK7QString(
    const QAxBase *self,
    const QString *verb) {
  return self->indexOfVerb(*verb);
}

//  void QAxBase::axBaseInit(QAxBasePrivate *b, IUnknown *iface)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAxBase10axBaseInitEP14QAxBasePrivateP8IUnknown(
    QAxBase *self,
    QAxBasePrivate *b,
    IUnknown *iface) {
  self->axBaseInit(b, iface);
}

//  bool QAxBase::initializeLicensedHelper(void *factory, const QString &key,
//      IUnknown **ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QAxBase24initializeLicensedHelperEPvRK7QStringPP8IUnknown(
    QAxBase *self,
    void *factory,
    const QString *key,
    IUnknown **ptr) {
  return self->initializeLicensedHelper(factory, *key, ptr);
}

//  int QAxBase::internalProperty(QMetaObject::Call a0, int index, void **v)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QAxBase16internalPropertyEN11QMetaObject4CallEiPPv(
    QAxBase *self,
    QMetaObject::Call a0,
    int index,
    void **v) {
  return self->internalProperty(a0, index, v);
}

//  int QAxBase::internalInvoke(QMetaObject::Call a0, int index, void **v)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QAxBase14internalInvokeEN11QMetaObject4CallEiPPv(
    QAxBase *self,
    QMetaObject::Call a0,
    int index,
    void **v) {
  return self->internalInvoke(a0, index, v);
}

//  a Python function taken by a CuteQAxBase, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxBase(QAxBase *self, const char *key, void *call) {
  return static_cast<CuteQAxBase *>(self)->take(key, call);
}

//  bool QAxBase::initialize(IUnknown **ptr)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QAxBase10initializeEPP8IUnknown(
    QAxBase *self,
    IUnknown **ptr) {
  return static_cast<OwnQAxBase *>(self)->OwnQAxBase::initialize(ptr);
}

#endif  // defined(Q_OS_WIN)
