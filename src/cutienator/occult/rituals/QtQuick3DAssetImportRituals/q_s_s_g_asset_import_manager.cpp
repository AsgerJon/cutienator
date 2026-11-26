//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DAsset
//  Import/6.12.0/QtQuick3DAssetImport/private/qssgassetimportmanager_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DAssetImport/6.12.0/QtQuick3DAssetImport/private/qtquick3dassetimportglobal_p.h>
#include <QtQuick3DAssetImport/QtQuick3DAssetImport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetImport/6.12.0/QtQuick3DAssetImport/private/qssgassetimportmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdir.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtCore/QHash>
#include <QtCore/QString>
#include <QtCore/QStringList>

//  A QSSGAssetImportManager that Python can take functions over in. Every QSSGAssetImportManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSSGAssetImportManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSSGAssetImportManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGAssetImportManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGAssetImportManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGAssetImportManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGAssetImportManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGAssetImportManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSSGAssetImportManager : public QSSGAssetImportManager {
public:
  using QSSGAssetImportManager::QSSGAssetImportManager;
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
      CuteQSSGAssetImportManagerCall0 call = reinterpret_cast<CuteQSSGAssetImportManagerCall0>(taken[0]);
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
      CuteQSSGAssetImportManagerCall1 call = reinterpret_cast<CuteQSSGAssetImportManagerCall1>(taken[1]);
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
      CuteQSSGAssetImportManagerCall2 call = reinterpret_cast<CuteQSSGAssetImportManagerCall2>(taken[2]);
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
      CuteQSSGAssetImportManagerCall3 call = reinterpret_cast<CuteQSSGAssetImportManagerCall3>(taken[3]);
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
      CuteQSSGAssetImportManagerCall4 call = reinterpret_cast<CuteQSSGAssetImportManagerCall4>(taken[4]);
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
      CuteQSSGAssetImportManagerCall5 call = reinterpret_cast<CuteQSSGAssetImportManagerCall5>(taken[5]);
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
      CuteQSSGAssetImportManagerCall6 call = reinterpret_cast<CuteQSSGAssetImportManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSSGAssetImportManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QSSGAssetImportManager10metaObjectEv(
    const QSSGAssetImportManager *self) {
  return self->metaObject();
}

//  void *QSSGAssetImportManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QSSGAssetImportManager11qt_metacastEPKc(
    QSSGAssetImportManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSSGAssetImportManager::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QSSGAssetImportManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QSSGAssetImportManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSSGAssetImportManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QSSGAssetImportManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSSGAssetImportManager::tr(s, c, n));
}

//  QSSGAssetImportManager::QSSGAssetImportManager(QObject *parent)
extern "C" Q_DECL_EXPORT
QSSGAssetImportManager *ritual_ZN22QSSGAssetImportManagerC1EP7QObject(
    QObject *parent) {
  return new CuteQSSGAssetImportManager(parent);
}

//  QSSGAssetImportManager::~QSSGAssetImportManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGAssetImportManagerD1Ev(QSSGAssetImportManager *self) {
  delete self;
}

//  ImportState QSSGAssetImportManager::importFile(const QString &filename,
//      const QDir &outputPath, QString *error)
extern "C" Q_DECL_EXPORT
QSSGAssetImportManager::ImportState ritual_ZN22QSSGAssetImportManager10importFileERK7QStringRK4QDirPS0_(
    QSSGAssetImportManager *self,
    const QString *filename,
    const QDir *outputPath,
    QString *error) {
  return self->importFile(*filename, *outputPath, error);
}

//  ImportState QSSGAssetImportManager::importFile(const QString &filename,
//      const QDir &outputPath, const QJsonObject &options, QString *error)
extern "C" Q_DECL_EXPORT
QSSGAssetImportManager::ImportState ritual_ZN22QSSGAssetImportManager10importFileERK7QStringRK4QDirRK11QJsonObjectPS0_(
    QSSGAssetImportManager *self,
    const QString *filename,
    const QDir *outputPath,
    const QJsonObject *options,
    QString *error) {
  return self->importFile(*filename, *outputPath, *options, error);
}

//  ImportState QSSGAssetImportManager::importFile(const QUrl &url,
//      QSSGSceneDesc::Scene &scene, QString *error)
extern "C" Q_DECL_EXPORT
QSSGAssetImportManager::ImportState ritual_ZN22QSSGAssetImportManager10importFileERK4QUrlRN13QSSGSceneDesc5SceneEP7QString(
    QSSGAssetImportManager *self,
    const QUrl *url,
    QSSGSceneDesc::Scene *scene,
    QString *error) {
  return self->importFile(*url, *scene, error);
}

//  ImportState QSSGAssetImportManager::importFile(const QUrl &url,
//      QSSGSceneDesc::Scene &scene, const QJsonObject &options, QString
//      *error)
extern "C" Q_DECL_EXPORT
QSSGAssetImportManager::ImportState ritual_ZN22QSSGAssetImportManager10importFileERK4QUrlRN13QSSGSceneDesc5SceneERK11QJsonObjectP7QString(
    QSSGAssetImportManager *self,
    const QUrl *url,
    QSSGSceneDesc::Scene *scene,
    const QJsonObject *options,
    QString *error) {
  return self->importFile(*url, *scene, *options, error);
}

//  QJsonObject QSSGAssetImportManager::getOptionsForFile(const QString
//      &filename)
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN22QSSGAssetImportManager17getOptionsForFileERK7QString(
    QSSGAssetImportManager *self,
    const QString *filename) {
  return new QJsonObject(self->getOptionsForFile(*filename));
}

//  PluginOptionMaps QSSGAssetImportManager::getAllOptions() const
extern "C" Q_DECL_EXPORT
QHash<QString, QJsonObject> *ritual_ZNK22QSSGAssetImportManager13getAllOptionsEv(
    const QSSGAssetImportManager *self) {
  return new QHash<QString, QJsonObject>(self->getAllOptions());
}

//  QHash<QString, QStringList>
//      QSSGAssetImportManager::getSupportedExtensions() const
extern "C" Q_DECL_EXPORT
QHash<QString, QStringList> *ritual_ZNK22QSSGAssetImportManager22getSupportedExtensionsEv(
    const QSSGAssetImportManager *self) {
  return new QHash<QString, QStringList>(self->getSupportedExtensions());
}

//  QList<QSSGAssetImporterPluginInfo>
//      QSSGAssetImportManager::getImporterPluginInfos() const
extern "C" Q_DECL_EXPORT
QList<QSSGAssetImporterPluginInfo> *ritual_ZNK22QSSGAssetImportManager22getImporterPluginInfosEv(
    const QSSGAssetImportManager *self) {
  return new QList<QSSGAssetImporterPluginInfo>(
      self->getImporterPluginInfos());
}

//  a Python function taken by a CuteQSSGAssetImportManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSSGAssetImportManager(
    QSSGAssetImportManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSSGAssetImportManager *>(self)->take(key, call);
}

//  a QHash<QString, QStringList> a ritual of QSSGAssetImportManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGAssetImportManager__QHash_QString_QStringList(
    QHash<QString, QStringList> *self) {
  delete self;
}
