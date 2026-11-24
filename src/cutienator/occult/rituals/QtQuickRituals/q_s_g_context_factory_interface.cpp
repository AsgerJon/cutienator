//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcontextplugin_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcontextplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <cstring>

//  A QSGContextFactoryInterface that Python can take functions over in. Every QSGContextFactoryInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGContextFactoryInterfaceCall0)(const void *, const QString *, int *);
typedef int (*CuteQSGContextFactoryInterfaceCall1)(const void *, const QString *, int *);
typedef void * (*CuteQSGContextFactoryInterfaceCall2)(const void *, const QImage *, int *);
typedef void * (*CuteQSGContextFactoryInterfaceCall3)(const void *, int *);
class CuteQSGContextFactoryInterface : public QSGContextFactoryInterface {
public:
  using QSGContextFactoryInterface::QSGContextFactoryInterface;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK26QSGContextFactoryInterface6createERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QSGContextFactoryInterface5flagsERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QSGContextFactoryInterface29createTextureFactoryFromImageERK6QImage")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QSGContextFactoryInterface19createWindowManagerEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  QSGContext *QSGContextFactoryInterface::create(const QString &key)
  //      const
  QSGContext *create(const QString &key) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGContextFactoryInterfaceCall0 call = reinterpret_cast<CuteQSGContextFactoryInterfaceCall0>(taken[0]);
      void * given = call(this, &key, &handled);
      if (handled) return static_cast<QSGContext *>(given);
    }
    return {};
  }

  //  Flags QSGContextFactoryInterface::flags(const QString &key) const
  QSGContextFactoryInterface::Flags flags(
      const QString &key) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGContextFactoryInterfaceCall1 call = reinterpret_cast<CuteQSGContextFactoryInterfaceCall1>(taken[1]);
      int given = call(this, &key, &handled);
      if (handled) return QFlags<QSGContextFactoryInterface::Flag>::fromInt(given);
    }
    return {};
  }

  //  QQuickTextureFactory
  //      *QSGContextFactoryInterface::createTextureFactoryFromImage(const
  //      QImage &image)
  QQuickTextureFactory *createTextureFactoryFromImage(
      const QImage &image) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGContextFactoryInterfaceCall2 call = reinterpret_cast<CuteQSGContextFactoryInterfaceCall2>(taken[2]);
      void * given = call(this, &image, &handled);
      if (handled) return static_cast<QQuickTextureFactory *>(given);
    }
    return {};
  }

  //  QSGRenderLoop *QSGContextFactoryInterface::createWindowManager()
  QSGRenderLoop *createWindowManager() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGContextFactoryInterfaceCall3 call = reinterpret_cast<CuteQSGContextFactoryInterfaceCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGRenderLoop *>(given);
    }
    return {};
  }
};

//  QSGContext *QSGContextFactoryInterface::create(const QString &key) const
extern "C" Q_DECL_EXPORT
QSGContext *ritual_ZNK26QSGContextFactoryInterface6createERK7QString(
    const QSGContextFactoryInterface *self,
    const QString *key) {
  return self->create(*key);
}

//  Flags QSGContextFactoryInterface::flags(const QString &key) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QSGContextFactoryInterface5flagsERK7QString(
    const QSGContextFactoryInterface *self,
    const QString *key) {
  return static_cast<int>(self->flags(*key).toInt());
}

//  QQuickTextureFactory
//      *QSGContextFactoryInterface::createTextureFactoryFromImage(const
//      QImage &image)
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_ZN26QSGContextFactoryInterface29createTextureFactoryFromImageERK6QImage(
    QSGContextFactoryInterface *self,
    const QImage *image) {
  return self->createTextureFactoryFromImage(*image);
}

//  QSGRenderLoop *QSGContextFactoryInterface::createWindowManager()
extern "C" Q_DECL_EXPORT
QSGRenderLoop *ritual_ZN26QSGContextFactoryInterface19createWindowManagerEv(
    QSGContextFactoryInterface *self) {
  return self->createWindowManager();
}

//  a Python function taken by a CuteQSGContextFactoryInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGContextFactoryInterface(
    QSGContextFactoryInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGContextFactoryInterface *>(self)->take(key, call);
}
