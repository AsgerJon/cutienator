//  Written by dev_tooling.RitualGenerator from the records of
//  QtUiTools/quiloader.h, Qt 6.12.0. Changes made here are lost.
#include <QtUiTools/quiloader.h>
#include <QtCore/qstring.h>
#include <QtCore/qdir.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QUiLoader that Python can take functions over in. Every QUiLoader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQUiLoaderCall0)(const void *, const QString *, QWidget *, const QString *, int *);
typedef void * (*CuteQUiLoaderCall1)(const void *, const QString *, QObject *, const QString *, int *);
typedef void * (*CuteQUiLoaderCall2)(const void *, QObject *, const QString *, int *);
typedef void * (*CuteQUiLoaderCall3)(const void *, QObject *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQUiLoaderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQUiLoaderCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUiLoaderCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUiLoaderCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUiLoaderCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUiLoaderCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUiLoaderCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQUiLoader : public QUiLoader {
public:
  using QUiLoader::QUiLoader;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QUiLoader12createWidgetERK7QStringP7QWidgetS2_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QUiLoader12createLayoutERK7QStringP7QObjectS2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QUiLoader17createActionGroupEP7QObjectRK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QUiLoader12createActionEP7QObjectRK7QString")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QWidget *QUiLoader::createWidget(const QString &className, QWidget
  //      *parent, const QString &name)
  QWidget *createWidget(
      const QString &className,
      QWidget *parent,
      const QString &name) override {
    if (taken[0]) {
      int handled = 0;
      CuteQUiLoaderCall0 call = reinterpret_cast<CuteQUiLoaderCall0>(taken[0]);
      void * given = call(this, &className, parent, &name, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QUiLoader::createWidget(className, parent, name);
  }

  //  QLayout *QUiLoader::createLayout(const QString &className, QObject
  //      *parent, const QString &name)
  QLayout *createLayout(
      const QString &className,
      QObject *parent,
      const QString &name) override {
    if (taken[1]) {
      int handled = 0;
      CuteQUiLoaderCall1 call = reinterpret_cast<CuteQUiLoaderCall1>(taken[1]);
      void * given = call(this, &className, parent, &name, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QUiLoader::createLayout(className, parent, name);
  }

  //  QActionGroup *QUiLoader::createActionGroup(QObject *parent, const
  //      QString &name)
  QActionGroup *createActionGroup(
      QObject *parent,
      const QString &name) override {
    if (taken[2]) {
      int handled = 0;
      CuteQUiLoaderCall2 call = reinterpret_cast<CuteQUiLoaderCall2>(taken[2]);
      void * given = call(this, parent, &name, &handled);
      if (handled) return static_cast<QActionGroup *>(given);
    }
    return QUiLoader::createActionGroup(parent, name);
  }

  //  QAction *QUiLoader::createAction(QObject *parent, const QString
  //      &name)
  QAction *createAction(QObject *parent, const QString &name) override {
    if (taken[3]) {
      int handled = 0;
      CuteQUiLoaderCall3 call = reinterpret_cast<CuteQUiLoaderCall3>(taken[3]);
      void * given = call(this, parent, &name, &handled);
      if (handled) return static_cast<QAction *>(given);
    }
    return QUiLoader::createAction(parent, name);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQUiLoaderCall4 call = reinterpret_cast<CuteQUiLoaderCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQUiLoaderCall5 call = reinterpret_cast<CuteQUiLoaderCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQUiLoaderCall6 call = reinterpret_cast<CuteQUiLoaderCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQUiLoaderCall7 call = reinterpret_cast<CuteQUiLoaderCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQUiLoaderCall8 call = reinterpret_cast<CuteQUiLoaderCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQUiLoaderCall9 call = reinterpret_cast<CuteQUiLoaderCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQUiLoaderCall10 call = reinterpret_cast<CuteQUiLoaderCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QUiLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QUiLoader10metaObjectEv(
    const QUiLoader *self) {
  return self->metaObject();
}

//  QString QUiLoader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QUiLoader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QUiLoader::tr(s, c, n));
}

//  QUiLoader::QUiLoader(QObject *parent)
extern "C" Q_DECL_EXPORT
QUiLoader *ritual_ZN9QUiLoaderC1EP7QObject(QObject *parent) {
  return new CuteQUiLoader(parent);
}

//  QUiLoader::~QUiLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUiLoaderD1Ev(QUiLoader *self) {
  delete self;
}

//  QStringList QUiLoader::pluginPaths() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QUiLoader11pluginPathsEv(const QUiLoader *self) {
  return new QList<QString>(self->pluginPaths());
}

//  void QUiLoader::clearPluginPaths()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUiLoader16clearPluginPathsEv(QUiLoader *self) {
  self->clearPluginPaths();
}

//  void QUiLoader::addPluginPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUiLoader13addPluginPathERK7QString(
    QUiLoader *self,
    const QString *path) {
  self->addPluginPath(*path);
}

//  QWidget *QUiLoader::load(QIODevice *device, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN9QUiLoader4loadEP9QIODeviceP7QWidget(
    QUiLoader *self,
    QIODevice *device,
    QWidget *parentWidget) {
  return self->load(device, parentWidget);
}

//  QStringList QUiLoader::availableWidgets() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QUiLoader16availableWidgetsEv(
    const QUiLoader *self) {
  return new QList<QString>(self->availableWidgets());
}

//  QStringList QUiLoader::availableLayouts() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QUiLoader16availableLayoutsEv(
    const QUiLoader *self) {
  return new QList<QString>(self->availableLayouts());
}

//  QWidget *QUiLoader::createWidget(const QString &className, QWidget
//      *parent, const QString &name)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN9QUiLoader12createWidgetERK7QStringP7QWidgetS2_(
    QUiLoader *self,
    const QString *className,
    QWidget *parent,
    const QString *name) {
  return self->createWidget(*className, parent, *name);
}

//  QLayout *QUiLoader::createLayout(const QString &className, QObject
//      *parent, const QString &name)
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN9QUiLoader12createLayoutERK7QStringP7QObjectS2_(
    QUiLoader *self,
    const QString *className,
    QObject *parent,
    const QString *name) {
  return self->createLayout(*className, parent, *name);
}

//  QActionGroup *QUiLoader::createActionGroup(QObject *parent, const QString
//      &name)
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_ZN9QUiLoader17createActionGroupEP7QObjectRK7QString(
    QUiLoader *self,
    QObject *parent,
    const QString *name) {
  return self->createActionGroup(parent, *name);
}

//  QAction *QUiLoader::createAction(QObject *parent, const QString &name)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN9QUiLoader12createActionEP7QObjectRK7QString(
    QUiLoader *self,
    QObject *parent,
    const QString *name) {
  return self->createAction(parent, *name);
}

//  void QUiLoader::setWorkingDirectory(const QDir &dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUiLoader19setWorkingDirectoryERK4QDir(
    QUiLoader *self,
    const QDir *dir) {
  self->setWorkingDirectory(*dir);
}

//  QDir QUiLoader::workingDirectory() const
extern "C" Q_DECL_EXPORT
QDir *ritual_ZNK9QUiLoader16workingDirectoryEv(const QUiLoader *self) {
  return new QDir(self->workingDirectory());
}

//  void QUiLoader::setLanguageChangeEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUiLoader24setLanguageChangeEnabledEb(
    QUiLoader *self,
    bool enabled) {
  self->setLanguageChangeEnabled(enabled);
}

//  bool QUiLoader::isLanguageChangeEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QUiLoader23isLanguageChangeEnabledEv(const QUiLoader *self) {
  return self->isLanguageChangeEnabled();
}

//  void QUiLoader::setTranslationEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUiLoader21setTranslationEnabledEb(
    QUiLoader *self,
    bool enabled) {
  self->setTranslationEnabled(enabled);
}

//  bool QUiLoader::isTranslationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QUiLoader20isTranslationEnabledEv(const QUiLoader *self) {
  return self->isTranslationEnabled();
}

//  QString QUiLoader::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QUiLoader11errorStringEv(const QUiLoader *self) {
  return new QString(self->errorString());
}

//  a Python function taken by a CuteQUiLoader, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUiLoader(QUiLoader *self, const char *key, void *call) {
  return static_cast<CuteQUiLoader *>(self)->take(key, call);
}

//  QWidget *QUiLoader::createWidget(const QString &className, QWidget
//      *parent, const QString &name)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN9QUiLoader12createWidgetERK7QStringP7QWidgetS2_(
    QUiLoader *self,
    const QString *className,
    QWidget *parent,
    const QString *name) {
  return self->QUiLoader::createWidget(*className, parent, *name);
}

//  QLayout *QUiLoader::createLayout(const QString &className, QObject
//      *parent, const QString &name)
extern "C" Q_DECL_EXPORT
QLayout *ritual_own_ZN9QUiLoader12createLayoutERK7QStringP7QObjectS2_(
    QUiLoader *self,
    const QString *className,
    QObject *parent,
    const QString *name) {
  return self->QUiLoader::createLayout(*className, parent, *name);
}

//  QActionGroup *QUiLoader::createActionGroup(QObject *parent, const QString
//      &name)
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_own_ZN9QUiLoader17createActionGroupEP7QObjectRK7QString(
    QUiLoader *self,
    QObject *parent,
    const QString *name) {
  return self->QUiLoader::createActionGroup(parent, *name);
}

//  QAction *QUiLoader::createAction(QObject *parent, const QString &name)
extern "C" Q_DECL_EXPORT
QAction *ritual_own_ZN9QUiLoader12createActionEP7QObjectRK7QString(
    QUiLoader *self,
    QObject *parent,
    const QString *name) {
  return self->QUiLoader::createAction(parent, *name);
}
