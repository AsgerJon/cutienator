//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/widgetdatabase_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/widgetdatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A qdesigner_internal::WidgetDataBase that Python can take functions over in. Every qdesigner_internal::WidgetDataBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*Cuteqdesigner_internal_WidgetDataBaseCall0)(const void *, int *);
typedef int (*Cuteqdesigner_internal_WidgetDataBaseCall1)(const void *, QObject *, bool, int *);
typedef int (*Cuteqdesigner_internal_WidgetDataBaseCall2)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_WidgetDataBaseCall3)(const void *, int, int *);
typedef int (*Cuteqdesigner_internal_WidgetDataBaseCall4)(const void *, QDesignerWidgetDataBaseItemInterface *, int *);
typedef void (*Cuteqdesigner_internal_WidgetDataBaseCall5)(const void *, int, QDesignerWidgetDataBaseItemInterface *, int *);
typedef void (*Cuteqdesigner_internal_WidgetDataBaseCall6)(const void *, QDesignerWidgetDataBaseItemInterface *, int *);
typedef int (*Cuteqdesigner_internal_WidgetDataBaseCall7)(const void *, const QString *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_WidgetDataBaseCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_WidgetDataBaseCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_WidgetDataBaseCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_WidgetDataBaseCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_WidgetDataBaseCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_WidgetDataBaseCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_WidgetDataBaseCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_WidgetDataBase : public qdesigner_internal::WidgetDataBase {
public:
  using qdesigner_internal::WidgetDataBase::WidgetDataBase;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface4coreEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface13indexOfObjectEP7QObjectb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface5countEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface4itemEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface7indexOfEP36QDesignerWidgetDataBaseItemInterface")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerWidgetDataBaseInterface6insertEiP36QDesignerWidgetDataBaseItemInterface")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerWidgetDataBaseInterface6appendEP36QDesignerWidgetDataBaseItemInterface")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface16indexOfClassNameERK7QStringb")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QDesignerFormEditorInterface
  //      *qdesigner_internal::WidgetDataBase::core() const
  QDesignerFormEditorInterface *core() const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall0 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return qdesigner_internal::WidgetDataBase::core();
  }

  //  int qdesigner_internal::WidgetDataBase::indexOfObject(QObject *o,
  //      bool resolveName) const
  int indexOfObject(QObject *o, bool resolveName) const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall1 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall1>(taken[1]);
      int given = call(this, o, resolveName, &handled);
      if (handled) return given;
    }
    return qdesigner_internal::WidgetDataBase::indexOfObject(o, resolveName);
  }

  //  int QDesignerWidgetDataBaseInterface::count() const
  int count() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall2 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDesignerWidgetDataBaseInterface::count();
  }

  //  QDesignerWidgetDataBaseItemInterface
  //      *QDesignerWidgetDataBaseInterface::item(int index) const
  QDesignerWidgetDataBaseItemInterface *item(int index) const override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall3 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall3>(taken[3]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QDesignerWidgetDataBaseItemInterface *>(given);
    }
    return QDesignerWidgetDataBaseInterface::item(index);
  }

  //  int QDesignerWidgetDataBaseInterface::indexOf(QDesignerWidgetDataBase
  //      ItemInterface *item) const
  int indexOf(QDesignerWidgetDataBaseItemInterface *item) const override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall4 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall4>(taken[4]);
      int given = call(this, item, &handled);
      if (handled) return given;
    }
    return QDesignerWidgetDataBaseInterface::indexOf(item);
  }

  //  void QDesignerWidgetDataBaseInterface::insert(int index,
  //      QDesignerWidgetDataBaseItemInterface *item)
  void insert(
      int index,
      QDesignerWidgetDataBaseItemInterface *item) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall5 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall5>(taken[5]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QDesignerWidgetDataBaseInterface::insert(index, item);
  }

  //  void QDesignerWidgetDataBaseInterface::append(QDesignerWidgetDataBase
  //      ItemInterface *item)
  void append(QDesignerWidgetDataBaseItemInterface *item) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall6 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall6>(taken[6]);
      call(this, item, &handled);
      if (handled) return;
    }
    QDesignerWidgetDataBaseInterface::append(item);
  }

  //  int QDesignerWidgetDataBaseInterface::indexOfClassName(const QString
  //      &className, bool resolveName) const
  int indexOfClassName(
      const QString &className,
      bool resolveName) const override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall7 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall7>(taken[7]);
      int given = call(this, &className, resolveName, &handled);
      if (handled) return given;
    }
    return QDesignerWidgetDataBaseInterface::indexOfClassName(className, resolveName);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall8 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall9 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall10 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall11 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall12 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall13 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetDataBaseCall14 call = reinterpret_cast<Cuteqdesigner_internal_WidgetDataBaseCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::WidgetDataBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14WidgetDataBase10metaObjectEv(
    const qdesigner_internal::WidgetDataBase *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::WidgetDataBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal14WidgetDataBase11qt_metacastEPKc(
    qdesigner_internal::WidgetDataBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::WidgetDataBase::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal14WidgetDataBase11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::WidgetDataBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::WidgetDataBase::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14WidgetDataBase2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::WidgetDataBase::tr(s, c, n));
}

//  qdesigner_internal::WidgetDataBase::WidgetDataBase(QDesignerFormEditorInt
//      erface *core, QObject *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::WidgetDataBase *ritual_ZN18qdesigner_internal14WidgetDataBaseC1EP28QDesignerFormEditorInterfaceP7QObject(
    QDesignerFormEditorInterface *core,
    QObject *parent) {
  return new Cuteqdesigner_internal_WidgetDataBase(core, parent);
}

//  qdesigner_internal::WidgetDataBase::~WidgetDataBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14WidgetDataBaseD1Ev(
    qdesigner_internal::WidgetDataBase *self) {
  delete self;
}

//  QDesignerFormEditorInterface *qdesigner_internal::WidgetDataBase::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK18qdesigner_internal14WidgetDataBase4coreEv(
    const qdesigner_internal::WidgetDataBase *self) {
  return self->core();
}

//  int qdesigner_internal::WidgetDataBase::indexOfObject(QObject *o, bool
//      resolveName) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal14WidgetDataBase13indexOfObjectEP7QObjectb(
    const qdesigner_internal::WidgetDataBase *self,
    QObject *o,
    bool resolveName) {
  return self->indexOfObject(o, resolveName);
}

//  void qdesigner_internal::WidgetDataBase::remove(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14WidgetDataBase6removeEi(
    qdesigner_internal::WidgetDataBase *self,
    int index) {
  self->remove(index);
}

//  void qdesigner_internal::WidgetDataBase::grabDefaultPropertyValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14WidgetDataBase25grabDefaultPropertyValuesEv(
    qdesigner_internal::WidgetDataBase *self) {
  self->grabDefaultPropertyValues();
}

//  void qdesigner_internal::WidgetDataBase::grabStandardWidgetBoxIcons()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14WidgetDataBase26grabStandardWidgetBoxIconsEv(
    qdesigner_internal::WidgetDataBase *self) {
  self->grabStandardWidgetBoxIcons();
}

//  QStringList qdesigner_internal::WidgetDataBase::formWidgetClasses(const
//      QDesignerFormEditorInterface *core)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN18qdesigner_internal14WidgetDataBase17formWidgetClassesEPK28QDesignerFormEditorInterface(
    const QDesignerFormEditorInterface *core) {
  return new QList<QString>(
      qdesigner_internal::WidgetDataBase::formWidgetClasses(
          core));
}

//  QStringList
//      qdesigner_internal::WidgetDataBase::customFormWidgetClasses(const
//      QDesignerFormEditorInterface *core)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN18qdesigner_internal14WidgetDataBase23customFormWidgetClassesEPK28QDesignerFormEditorInterface(
    const QDesignerFormEditorInterface *core) {
  return new QList<QString>(
      qdesigner_internal::WidgetDataBase::customFormWidgetClasses(
          core));
}

//  QString qdesigner_internal::WidgetDataBase::formTemplate(const
//      QDesignerFormEditorInterface *core, const QString &className, const
//      QString &objectName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14WidgetDataBase12formTemplateEPK28QDesignerFormEditorInterfaceRK7QStringS6_(
    const QDesignerFormEditorInterface *core,
    const QString *className,
    const QString *objectName) {
  return new QString(
      qdesigner_internal::WidgetDataBase::formTemplate(
          core,
          *className,
          *objectName));
}

//  QString qdesigner_internal::WidgetDataBase::scaleFormTemplate(const
//      QString &xml, const QSize &size, bool fixed)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14WidgetDataBase17scaleFormTemplateERK7QStringRK5QSizeb(
    const QString *xml,
    const QSize *size,
    bool fixed) {
  return new QString(
      qdesigner_internal::WidgetDataBase::scaleFormTemplate(
          *xml,
          *size,
          fixed));
}

//  void qdesigner_internal::WidgetDataBase::loadPlugins()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14WidgetDataBase11loadPluginsEv(
    qdesigner_internal::WidgetDataBase *self) {
  self->loadPlugins();
}

//  QList<QVariant>
//      qdesigner_internal::WidgetDataBase::defaultPropertyValues(const
//      QString &name)
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZN18qdesigner_internal14WidgetDataBase21defaultPropertyValuesERK7QString(
    qdesigner_internal::WidgetDataBase *self,
    const QString *name) {
  return new QList<QVariant>(self->defaultPropertyValues(*name));
}

//  a Python function taken by a Cuteqdesigner_internal_WidgetDataBase, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_WidgetDataBase(
    qdesigner_internal::WidgetDataBase *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_WidgetDataBase *>(self)->take(key, call);
}

//  QDesignerFormEditorInterface *qdesigner_internal::WidgetDataBase::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_own_ZNK18qdesigner_internal14WidgetDataBase4coreEv(
    const qdesigner_internal::WidgetDataBase *self) {
  return self->qdesigner_internal::WidgetDataBase::core();
}

//  int qdesigner_internal::WidgetDataBase::indexOfObject(QObject *o, bool
//      resolveName) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18qdesigner_internal14WidgetDataBase13indexOfObjectEP7QObjectb(
    const qdesigner_internal::WidgetDataBase *self,
    QObject *o,
    bool resolveName) {
  return self->qdesigner_internal::WidgetDataBase::indexOfObject(
      o,
      resolveName);
}
