//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qtresourcemodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qtresourcemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QMap>
#include <QtCore/QString>

//  A QtResourceModel that Python can take functions over in. Every QtResourceModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtResourceModelCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtResourceModelCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtResourceModelCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtResourceModelCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtResourceModelCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtResourceModelCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtResourceModelCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtResourceModel : public QtResourceModel {
public:
  using QtResourceModel::QtResourceModel;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtResourceModelCall0 call = reinterpret_cast<CuteQtResourceModelCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtResourceModelCall1 call = reinterpret_cast<CuteQtResourceModelCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtResourceModelCall2 call = reinterpret_cast<CuteQtResourceModelCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtResourceModelCall3 call = reinterpret_cast<CuteQtResourceModelCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtResourceModelCall4 call = reinterpret_cast<CuteQtResourceModelCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQtResourceModelCall5 call = reinterpret_cast<CuteQtResourceModelCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtResourceModelCall6 call = reinterpret_cast<CuteQtResourceModelCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtResourceModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QtResourceModel10metaObjectEv(
    const QtResourceModel *self) {
  return self->metaObject();
}

//  void *QtResourceModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QtResourceModel11qt_metacastEPKc(
    QtResourceModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtResourceModel::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QtResourceModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QtResourceModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtResourceModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QtResourceModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtResourceModel::tr(s, c, n));
}

//  QtResourceModel::QtResourceModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QtResourceModel *ritual_ZN15QtResourceModelC1EP7QObject(QObject *parent) {
  return new CuteQtResourceModel(parent);
}

//  QtResourceModel::~QtResourceModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtResourceModelD1Ev(QtResourceModel *self) {
  delete self;
}

//  QStringList QtResourceModel::loadedQrcFiles() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QtResourceModel14loadedQrcFilesEv(
    const QtResourceModel *self) {
  return new QList<QString>(self->loadedQrcFiles());
}

//  bool QtResourceModel::isModified(const QString &path) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QtResourceModel10isModifiedERK7QString(
    const QtResourceModel *self,
    const QString *path) {
  return self->isModified(*path);
}

//  void QtResourceModel::setModified(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtResourceModel11setModifiedERK7QString(
    QtResourceModel *self,
    const QString *path) {
  self->setModified(*path);
}

//  QList<QtResourceSet *> QtResourceModel::resourceSets() const
extern "C" Q_DECL_EXPORT
QList<QtResourceSet *> *ritual_ZNK15QtResourceModel12resourceSetsEv(
    const QtResourceModel *self) {
  return new QList<QtResourceSet *>(self->resourceSets());
}

//  QtResourceSet *QtResourceModel::currentResourceSet() const
extern "C" Q_DECL_EXPORT
QtResourceSet *ritual_ZNK15QtResourceModel18currentResourceSetEv(
    const QtResourceModel *self) {
  return self->currentResourceSet();
}

//  void QtResourceModel::setCurrentResourceSet(QtResourceSet *resourceSet,
//      int *errorCount, QString *errorMessages)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtResourceModel21setCurrentResourceSetEP13QtResourceSetPiP7QString(
    QtResourceModel *self,
    QtResourceSet *resourceSet,
    int *errorCount,
    QString *errorMessages) {
  self->setCurrentResourceSet(resourceSet, errorCount, errorMessages);
}

//  QtResourceSet *QtResourceModel::addResourceSet(const QStringList &paths)
extern "C" Q_DECL_EXPORT
QtResourceSet *ritual_ZN15QtResourceModel14addResourceSetERK5QListI7QStringE(
    QtResourceModel *self,
    const QList<QString> *paths) {
  return self->addResourceSet(*paths);
}

//  void QtResourceModel::removeResourceSet(QtResourceSet *resourceSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtResourceModel17removeResourceSetEP13QtResourceSet(
    QtResourceModel *self,
    QtResourceSet *resourceSet) {
  self->removeResourceSet(resourceSet);
}

//  void QtResourceModel::reload(const QString &path, int *errorCount,
//      QString *errorMessages)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtResourceModel6reloadERK7QStringPiPS0_(
    QtResourceModel *self,
    const QString *path,
    int *errorCount,
    QString *errorMessages) {
  self->reload(*path, errorCount, errorMessages);
}

//  void QtResourceModel::reload(int *errorCount, QString *errorMessages)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtResourceModel6reloadEPiP7QString(
    QtResourceModel *self,
    int *errorCount,
    QString *errorMessages) {
  self->reload(errorCount, errorMessages);
}

//  QMap<QString, QString> QtResourceModel::contents() const
extern "C" Q_DECL_EXPORT
QMap<QString, QString> *ritual_ZNK15QtResourceModel8contentsEv(
    const QtResourceModel *self) {
  return new QMap<QString, QString>(self->contents());
}

//  QString QtResourceModel::qrcPath(const QString &file) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QtResourceModel7qrcPathERK7QString(
    const QtResourceModel *self,
    const QString *file) {
  return new QString(self->qrcPath(*file));
}

//  void QtResourceModel::setWatcherEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtResourceModel17setWatcherEnabledEb(
    QtResourceModel *self,
    bool enable) {
  self->setWatcherEnabled(enable);
}

//  bool QtResourceModel::isWatcherEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QtResourceModel16isWatcherEnabledEv(
    const QtResourceModel *self) {
  return self->isWatcherEnabled();
}

//  void QtResourceModel::setWatcherEnabled(const QString &path, bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtResourceModel17setWatcherEnabledERK7QStringb(
    QtResourceModel *self,
    const QString *path,
    bool enable) {
  self->setWatcherEnabled(*path, enable);
}

//  bool QtResourceModel::isWatcherEnabled(const QString &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QtResourceModel16isWatcherEnabledERK7QString(
    QtResourceModel *self,
    const QString *path) {
  return self->isWatcherEnabled(*path);
}

//  void QtResourceModel::resourceSetActivated(QtResourceSet *resourceSet,
//      bool resourceSetChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtResourceModel20resourceSetActivatedEP13QtResourceSetb(
    QtResourceModel *self,
    QtResourceSet *resourceSet,
    bool resourceSetChanged) {
  self->resourceSetActivated(resourceSet, resourceSetChanged);
}

//  void QtResourceModel::qrcFileModifiedExternally(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtResourceModel25qrcFileModifiedExternallyERK7QString(
    QtResourceModel *self,
    const QString *path) {
  self->qrcFileModifiedExternally(*path);
}

//  QtResourceModelPrivate *QtResourceModel::d_func()
extern "C" Q_DECL_EXPORT
QtResourceModelPrivate *ritual_ZN15QtResourceModel6d_funcEv(
    QtResourceModel *self) {
  return self->d_func();
}

//  const QtResourceModelPrivate *QtResourceModel::d_func() const
extern "C" Q_DECL_EXPORT
const QtResourceModelPrivate *ritual_ZNK15QtResourceModel6d_funcEv(
    const QtResourceModel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQtResourceModel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtResourceModel(
    QtResourceModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtResourceModel *>(self)->take(key, call);
}

//  a QMap<QString, QString> a ritual of QtResourceModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtResourceModel__QMap_QString_QString(
    QMap<QString, QString> *self) {
  delete self;
}
