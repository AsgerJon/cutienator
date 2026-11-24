//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractwidgetdatabase.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDesigner/abstractwidgetdatabase.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDesignerWidgetDataBaseInterface that Python can take functions over in. Every QDesignerWidgetDataBaseInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQDesignerWidgetDataBaseInterfaceCall0)(const void *, int *);
typedef void * (*CuteQDesignerWidgetDataBaseInterfaceCall1)(const void *, int, int *);
typedef int (*CuteQDesignerWidgetDataBaseInterfaceCall2)(const void *, QDesignerWidgetDataBaseItemInterface *, int *);
typedef void (*CuteQDesignerWidgetDataBaseInterfaceCall3)(const void *, int, QDesignerWidgetDataBaseItemInterface *, int *);
typedef void (*CuteQDesignerWidgetDataBaseInterfaceCall4)(const void *, QDesignerWidgetDataBaseItemInterface *, int *);
typedef int (*CuteQDesignerWidgetDataBaseInterfaceCall5)(const void *, QObject *, bool, int *);
typedef int (*CuteQDesignerWidgetDataBaseInterfaceCall6)(const void *, const QString *, bool, int *);
typedef void * (*CuteQDesignerWidgetDataBaseInterfaceCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerWidgetDataBaseInterfaceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerWidgetDataBaseInterfaceCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetDataBaseInterfaceCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetDataBaseInterfaceCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetDataBaseInterfaceCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetDataBaseInterfaceCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetDataBaseInterfaceCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerWidgetDataBaseInterface : public QDesignerWidgetDataBaseInterface {
public:
  using QDesignerWidgetDataBaseInterface::QDesignerWidgetDataBaseInterface;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface5countEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface4itemEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface7indexOfEP36QDesignerWidgetDataBaseItemInterface")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerWidgetDataBaseInterface6insertEiP36QDesignerWidgetDataBaseItemInterface")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerWidgetDataBaseInterface6appendEP36QDesignerWidgetDataBaseItemInterface")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface13indexOfObjectEP7QObjectb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface16indexOfClassNameERK7QStringb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerWidgetDataBaseInterface4coreEv")) {
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

  //  int QDesignerWidgetDataBaseInterface::count() const
  int count() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseInterfaceCall0 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDesignerWidgetDataBaseInterface::count();
  }

  //  QDesignerWidgetDataBaseItemInterface
  //      *QDesignerWidgetDataBaseInterface::item(int index) const
  QDesignerWidgetDataBaseItemInterface *item(int index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseInterfaceCall1 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall1>(taken[1]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QDesignerWidgetDataBaseItemInterface *>(given);
    }
    return QDesignerWidgetDataBaseInterface::item(index);
  }

  //  int QDesignerWidgetDataBaseInterface::indexOf(QDesignerWidgetDataBase
  //      ItemInterface *item) const
  int indexOf(QDesignerWidgetDataBaseItemInterface *item) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseInterfaceCall2 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseInterfaceCall3 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall3>(taken[3]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QDesignerWidgetDataBaseInterface::insert(index, item);
  }

  //  void QDesignerWidgetDataBaseInterface::append(QDesignerWidgetDataBase
  //      ItemInterface *item)
  void append(QDesignerWidgetDataBaseItemInterface *item) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseInterfaceCall4 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall4>(taken[4]);
      call(this, item, &handled);
      if (handled) return;
    }
    QDesignerWidgetDataBaseInterface::append(item);
  }

  //  int QDesignerWidgetDataBaseInterface::indexOfObject(QObject *object,
  //      bool resolveName) const
  int indexOfObject(QObject *object, bool resolveName) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseInterfaceCall5 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall5>(taken[5]);
      int given = call(this, object, resolveName, &handled);
      if (handled) return given;
    }
    return QDesignerWidgetDataBaseInterface::indexOfObject(object, resolveName);
  }

  //  int QDesignerWidgetDataBaseInterface::indexOfClassName(const QString
  //      &className, bool resolveName) const
  int indexOfClassName(
      const QString &className,
      bool resolveName) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseInterfaceCall6 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall6>(taken[6]);
      int given = call(this, &className, resolveName, &handled);
      if (handled) return given;
    }
    return QDesignerWidgetDataBaseInterface::indexOfClassName(className, resolveName);
  }

  //  QDesignerFormEditorInterface
  //      *QDesignerWidgetDataBaseInterface::core() const
  QDesignerFormEditorInterface *core() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseInterfaceCall7 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return QDesignerWidgetDataBaseInterface::core();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseInterfaceCall8 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall8>(taken[8]);
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
      CuteQDesignerWidgetDataBaseInterfaceCall9 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall9>(taken[9]);
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
      CuteQDesignerWidgetDataBaseInterfaceCall10 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall10>(taken[10]);
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
      CuteQDesignerWidgetDataBaseInterfaceCall11 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall11>(taken[11]);
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
      CuteQDesignerWidgetDataBaseInterfaceCall12 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall12>(taken[12]);
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
      CuteQDesignerWidgetDataBaseInterfaceCall13 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall13>(taken[13]);
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
      CuteQDesignerWidgetDataBaseInterfaceCall14 call = reinterpret_cast<CuteQDesignerWidgetDataBaseInterfaceCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerWidgetDataBaseInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QDesignerWidgetDataBaseInterface10metaObjectEv(
    const QDesignerWidgetDataBaseInterface *self) {
  return self->metaObject();
}

//  QString QDesignerWidgetDataBaseInterface::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QDesignerWidgetDataBaseInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerWidgetDataBaseInterface::tr(s, c, n));
}

//  QDesignerWidgetDataBaseInterface::QDesignerWidgetDataBaseInterface(QObjec
//      t *parent)
extern "C" Q_DECL_EXPORT
QDesignerWidgetDataBaseInterface *ritual_ZN32QDesignerWidgetDataBaseInterfaceC1EP7QObject(
    QObject *parent) {
  return new CuteQDesignerWidgetDataBaseInterface(parent);
}

//  QDesignerWidgetDataBaseInterface::~QDesignerWidgetDataBaseInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerWidgetDataBaseInterfaceD1Ev(
    QDesignerWidgetDataBaseInterface *self) {
  delete self;
}

//  int QDesignerWidgetDataBaseInterface::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QDesignerWidgetDataBaseInterface5countEv(
    const QDesignerWidgetDataBaseInterface *self) {
  return self->count();
}

//  QDesignerWidgetDataBaseItemInterface
//      *QDesignerWidgetDataBaseInterface::item(int index) const
extern "C" Q_DECL_EXPORT
QDesignerWidgetDataBaseItemInterface *ritual_ZNK32QDesignerWidgetDataBaseInterface4itemEi(
    const QDesignerWidgetDataBaseInterface *self,
    int index) {
  return self->item(index);
}

//  int QDesignerWidgetDataBaseInterface::indexOf(QDesignerWidgetDataBaseItem
//      Interface *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QDesignerWidgetDataBaseInterface7indexOfEP36QDesignerWidgetDataBaseItemInterface(
    const QDesignerWidgetDataBaseInterface *self,
    QDesignerWidgetDataBaseItemInterface *item) {
  return self->indexOf(item);
}

//  void QDesignerWidgetDataBaseInterface::insert(int index,
//      QDesignerWidgetDataBaseItemInterface *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerWidgetDataBaseInterface6insertEiP36QDesignerWidgetDataBaseItemInterface(
    QDesignerWidgetDataBaseInterface *self,
    int index,
    QDesignerWidgetDataBaseItemInterface *item) {
  self->insert(index, item);
}

//  void QDesignerWidgetDataBaseInterface::append(QDesignerWidgetDataBaseItem
//      Interface *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerWidgetDataBaseInterface6appendEP36QDesignerWidgetDataBaseItemInterface(
    QDesignerWidgetDataBaseInterface *self,
    QDesignerWidgetDataBaseItemInterface *item) {
  self->append(item);
}

//  int QDesignerWidgetDataBaseInterface::indexOfObject(QObject *object, bool
//      resolveName) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QDesignerWidgetDataBaseInterface13indexOfObjectEP7QObjectb(
    const QDesignerWidgetDataBaseInterface *self,
    QObject *object,
    bool resolveName) {
  return self->indexOfObject(object, resolveName);
}

//  int QDesignerWidgetDataBaseInterface::indexOfClassName(const QString
//      &className, bool resolveName) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QDesignerWidgetDataBaseInterface16indexOfClassNameERK7QStringb(
    const QDesignerWidgetDataBaseInterface *self,
    const QString *className,
    bool resolveName) {
  return self->indexOfClassName(*className, resolveName);
}

//  QDesignerFormEditorInterface *QDesignerWidgetDataBaseInterface::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK32QDesignerWidgetDataBaseInterface4coreEv(
    const QDesignerWidgetDataBaseInterface *self) {
  return self->core();
}

//  bool QDesignerWidgetDataBaseInterface::isContainer(QObject *object, bool
//      resolveName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QDesignerWidgetDataBaseInterface11isContainerEP7QObjectb(
    const QDesignerWidgetDataBaseInterface *self,
    QObject *object,
    bool resolveName) {
  return self->isContainer(object, resolveName);
}

//  bool QDesignerWidgetDataBaseInterface::isCustom(QObject *object, bool
//      resolveName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QDesignerWidgetDataBaseInterface8isCustomEP7QObjectb(
    const QDesignerWidgetDataBaseInterface *self,
    QObject *object,
    bool resolveName) {
  return self->isCustom(object, resolveName);
}

//  a Python function taken by a CuteQDesignerWidgetDataBaseInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerWidgetDataBaseInterface(
    QDesignerWidgetDataBaseInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerWidgetDataBaseInterface *>(self)->take(key, call);
}

//  int QDesignerWidgetDataBaseInterface::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK32QDesignerWidgetDataBaseInterface5countEv(
    const QDesignerWidgetDataBaseInterface *self) {
  return self->QDesignerWidgetDataBaseInterface::count();
}

//  QDesignerWidgetDataBaseItemInterface
//      *QDesignerWidgetDataBaseInterface::item(int index) const
extern "C" Q_DECL_EXPORT
QDesignerWidgetDataBaseItemInterface *ritual_own_ZNK32QDesignerWidgetDataBaseInterface4itemEi(
    const QDesignerWidgetDataBaseInterface *self,
    int index) {
  return self->QDesignerWidgetDataBaseInterface::item(index);
}

//  int QDesignerWidgetDataBaseInterface::indexOf(QDesignerWidgetDataBaseItem
//      Interface *item) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK32QDesignerWidgetDataBaseInterface7indexOfEP36QDesignerWidgetDataBaseItemInterface(
    const QDesignerWidgetDataBaseInterface *self,
    QDesignerWidgetDataBaseItemInterface *item) {
  return self->QDesignerWidgetDataBaseInterface::indexOf(item);
}

//  void QDesignerWidgetDataBaseInterface::insert(int index,
//      QDesignerWidgetDataBaseItemInterface *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QDesignerWidgetDataBaseInterface6insertEiP36QDesignerWidgetDataBaseItemInterface(
    QDesignerWidgetDataBaseInterface *self,
    int index,
    QDesignerWidgetDataBaseItemInterface *item) {
  self->QDesignerWidgetDataBaseInterface::insert(index, item);
}

//  void QDesignerWidgetDataBaseInterface::append(QDesignerWidgetDataBaseItem
//      Interface *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QDesignerWidgetDataBaseInterface6appendEP36QDesignerWidgetDataBaseItemInterface(
    QDesignerWidgetDataBaseInterface *self,
    QDesignerWidgetDataBaseItemInterface *item) {
  self->QDesignerWidgetDataBaseInterface::append(item);
}

//  int QDesignerWidgetDataBaseInterface::indexOfObject(QObject *object, bool
//      resolveName) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK32QDesignerWidgetDataBaseInterface13indexOfObjectEP7QObjectb(
    const QDesignerWidgetDataBaseInterface *self,
    QObject *object,
    bool resolveName) {
  return self->QDesignerWidgetDataBaseInterface::indexOfObject(
      object,
      resolveName);
}

//  int QDesignerWidgetDataBaseInterface::indexOfClassName(const QString
//      &className, bool resolveName) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK32QDesignerWidgetDataBaseInterface16indexOfClassNameERK7QStringb(
    const QDesignerWidgetDataBaseInterface *self,
    const QString *className,
    bool resolveName) {
  return self->QDesignerWidgetDataBaseInterface::indexOfClassName(
      *className,
      resolveName);
}

//  QDesignerFormEditorInterface *QDesignerWidgetDataBaseInterface::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_own_ZNK32QDesignerWidgetDataBaseInterface4coreEv(
    const QDesignerWidgetDataBaseInterface *self) {
  return self->QDesignerWidgetDataBaseInterface::core();
}
