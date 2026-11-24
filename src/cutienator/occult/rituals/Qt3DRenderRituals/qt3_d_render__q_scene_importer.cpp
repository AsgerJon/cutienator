//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qsceneimporter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qsceneimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Qt3DRender::QSceneImporter that Python can take functions over in. Every Qt3DRender::QSceneImporter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QSceneImporterCall0)(const void *, const QUrl *, int *);
typedef void (*CuteQt3DRender_QSceneImporterCall1)(const void *, const QByteArray *, const QString *, int *);
typedef void * (*CuteQt3DRender_QSceneImporterCall2)(const void *, const QString *, int *);
typedef void * (*CuteQt3DRender_QSceneImporterCall3)(const void *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QSceneImporterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QSceneImporterCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSceneImporterCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSceneImporterCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSceneImporterCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSceneImporterCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSceneImporterCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QSceneImporter : public Qt3DRender::QSceneImporter {
public:
  using Qt3DRender::QSceneImporter::QSceneImporter;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender14QSceneImporter9setSourceERK4QUrl")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender14QSceneImporter7setDataERK10QByteArrayRK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender14QSceneImporter5sceneERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender14QSceneImporter4nodeERK7QString")) {
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

  //  void Qt3DRender::QSceneImporter::setSource(const QUrl &source)
  void setSource(const QUrl &source) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QSceneImporterCall0 call = reinterpret_cast<CuteQt3DRender_QSceneImporterCall0>(taken[0]);
      call(this, &source, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::QSceneImporter::setData(const QByteArray &data,
  //      const QString &basePath)
  void setData(const QByteArray &data, const QString &basePath) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QSceneImporterCall1 call = reinterpret_cast<CuteQt3DRender_QSceneImporterCall1>(taken[1]);
      call(this, &data, &basePath, &handled);
      if (handled) return;
    }
  }

  //  Qt3DCore::QEntity *Qt3DRender::QSceneImporter::scene(const QString
  //      &id)
  Qt3DCore::QEntity *scene(const QString &id) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QSceneImporterCall2 call = reinterpret_cast<CuteQt3DRender_QSceneImporterCall2>(taken[2]);
      void * given = call(this, &id, &handled);
      if (handled) return static_cast<Qt3DCore::QEntity *>(given);
    }
    return {};
  }

  //  Qt3DCore::QEntity *Qt3DRender::QSceneImporter::node(const QString
  //      &id)
  Qt3DCore::QEntity *node(const QString &id) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_QSceneImporterCall3 call = reinterpret_cast<CuteQt3DRender_QSceneImporterCall3>(taken[3]);
      void * given = call(this, &id, &handled);
      if (handled) return static_cast<Qt3DCore::QEntity *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_QSceneImporterCall4 call = reinterpret_cast<CuteQt3DRender_QSceneImporterCall4>(taken[4]);
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
      CuteQt3DRender_QSceneImporterCall5 call = reinterpret_cast<CuteQt3DRender_QSceneImporterCall5>(taken[5]);
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
      CuteQt3DRender_QSceneImporterCall6 call = reinterpret_cast<CuteQt3DRender_QSceneImporterCall6>(taken[6]);
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
      CuteQt3DRender_QSceneImporterCall7 call = reinterpret_cast<CuteQt3DRender_QSceneImporterCall7>(taken[7]);
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
      CuteQt3DRender_QSceneImporterCall8 call = reinterpret_cast<CuteQt3DRender_QSceneImporterCall8>(taken[8]);
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
      CuteQt3DRender_QSceneImporterCall9 call = reinterpret_cast<CuteQt3DRender_QSceneImporterCall9>(taken[9]);
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
      CuteQt3DRender_QSceneImporterCall10 call = reinterpret_cast<CuteQt3DRender_QSceneImporterCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QSceneImporter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender14QSceneImporter10metaObjectEv(
    const Qt3DRender::QSceneImporter *self) {
  return self->metaObject();
}

//  QString Qt3DRender::QSceneImporter::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender14QSceneImporter2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QSceneImporter::tr(s, c, n));
}

//  Qt3DRender::QSceneImporter::~QSceneImporter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QSceneImporterD1Ev(
    Qt3DRender::QSceneImporter *self) {
  delete self;
}

//  void Qt3DRender::QSceneImporter::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QSceneImporter9setSourceERK4QUrl(
    Qt3DRender::QSceneImporter *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  void Qt3DRender::QSceneImporter::setData(const QByteArray &data, const
//      QString &basePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QSceneImporter7setDataERK10QByteArrayRK7QString(
    Qt3DRender::QSceneImporter *self,
    const QByteArray *data,
    const QString *basePath) {
  self->setData(*data, *basePath);
}

//  bool Qt3DRender::QSceneImporter::areFileTypesSupported(const QStringList
//      &extensions) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender14QSceneImporter21areFileTypesSupportedERK5QListI7QStringE(
    const Qt3DRender::QSceneImporter *self,
    const QList<QString> *extensions) {
  return self->areFileTypesSupported(*extensions);
}

//  Qt3DCore::QEntity *Qt3DRender::QSceneImporter::scene(const QString &id)
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZN10Qt3DRender14QSceneImporter5sceneERK7QString(
    Qt3DRender::QSceneImporter *self,
    const QString *id) {
  return self->scene(*id);
}

//  Qt3DCore::QEntity *Qt3DRender::QSceneImporter::node(const QString &id)
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZN10Qt3DRender14QSceneImporter4nodeERK7QString(
    Qt3DRender::QSceneImporter *self,
    const QString *id) {
  return self->node(*id);
}

//  a Python function taken by a CuteQt3DRender_QSceneImporter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QSceneImporter(
    Qt3DRender::QSceneImporter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QSceneImporter *>(self)->take(key, call);
}
