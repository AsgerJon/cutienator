//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qcustom3ditem.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qcustom3ditem.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QCustom3DItem that Python can take functions over in. Every QCustom3DItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DItemCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DItemCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DItemCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DItemCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DItemCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DItemCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DItemCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCustom3DItem : public QCustom3DItem {
public:
  using QCustom3DItem::QCustom3DItem;
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
      CuteQCustom3DItemCall0 call = reinterpret_cast<CuteQCustom3DItemCall0>(taken[0]);
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
      CuteQCustom3DItemCall1 call = reinterpret_cast<CuteQCustom3DItemCall1>(taken[1]);
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
      CuteQCustom3DItemCall2 call = reinterpret_cast<CuteQCustom3DItemCall2>(taken[2]);
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
      CuteQCustom3DItemCall3 call = reinterpret_cast<CuteQCustom3DItemCall3>(taken[3]);
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
      CuteQCustom3DItemCall4 call = reinterpret_cast<CuteQCustom3DItemCall4>(taken[4]);
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
      CuteQCustom3DItemCall5 call = reinterpret_cast<CuteQCustom3DItemCall5>(taken[5]);
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
      CuteQCustom3DItemCall6 call = reinterpret_cast<CuteQCustom3DItemCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCustom3DItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QCustom3DItem10metaObjectEv(
    const QCustom3DItem *self) {
  return self->metaObject();
}

//  void *QCustom3DItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QCustom3DItem11qt_metacastEPKc(
    QCustom3DItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCustom3DItem::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QCustom3DItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QCustom3DItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCustom3DItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QCustom3DItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCustom3DItem::tr(s, c, n));
}

//  QCustom3DItemPrivate *QCustom3DItem::d_func()
extern "C" Q_DECL_EXPORT
QCustom3DItemPrivate *ritual_ZN13QCustom3DItem6d_funcEv(
    QCustom3DItem *self) {
  return self->d_func();
}

//  const QCustom3DItemPrivate *QCustom3DItem::d_func() const
extern "C" Q_DECL_EXPORT
const QCustom3DItemPrivate *ritual_ZNK13QCustom3DItem6d_funcEv(
    const QCustom3DItem *self) {
  return self->d_func();
}

//  QCustom3DItem::QCustom3DItem(QObject *parent)
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZN13QCustom3DItemC1EP7QObject(QObject *parent) {
  return new CuteQCustom3DItem(parent);
}

//  QCustom3DItem::QCustom3DItem(const QString &meshFile, QVector3D position,
//      QVector3D scaling, const QQuaternion &rotation, const QImage
//      &texture, QObject *parent)
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZN13QCustom3DItemC1ERK7QString9QVector3DS3_RK11QQuaternionRK6QImageP7QObject(
    const QString *meshFile,
    const QVector3D *position,
    const QVector3D *scaling,
    const QQuaternion *rotation,
    const QImage *texture,
    QObject *parent) {
  return new CuteQCustom3DItem(
      *meshFile,
      *position,
      *scaling,
      *rotation,
      *texture,
      parent);
}

//  QCustom3DItem::~QCustom3DItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItemD1Ev(QCustom3DItem *self) {
  delete self;
}

//  void QCustom3DItem::setMeshFile(const QString &meshFile)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem11setMeshFileERK7QString(
    QCustom3DItem *self,
    const QString *meshFile) {
  self->setMeshFile(*meshFile);
}

//  QString QCustom3DItem::meshFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QCustom3DItem8meshFileEv(const QCustom3DItem *self) {
  return new QString(self->meshFile());
}

//  void QCustom3DItem::setTextureFile(const QString &textureFile)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem14setTextureFileERK7QString(
    QCustom3DItem *self,
    const QString *textureFile) {
  self->setTextureFile(*textureFile);
}

//  QString QCustom3DItem::textureFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QCustom3DItem11textureFileEv(
    const QCustom3DItem *self) {
  return new QString(self->textureFile());
}

//  void QCustom3DItem::setPosition(QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem11setPositionE9QVector3D(
    QCustom3DItem *self,
    const QVector3D *position) {
  self->setPosition(*position);
}

//  QVector3D QCustom3DItem::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK13QCustom3DItem8positionEv(const QCustom3DItem *self) {
  return new QVector3D(self->position());
}

//  void QCustom3DItem::setPositionAbsolute(bool positionAbsolute)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem19setPositionAbsoluteEb(
    QCustom3DItem *self,
    bool positionAbsolute) {
  self->setPositionAbsolute(positionAbsolute);
}

//  bool QCustom3DItem::isPositionAbsolute() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCustom3DItem18isPositionAbsoluteEv(
    const QCustom3DItem *self) {
  return self->isPositionAbsolute();
}

//  void QCustom3DItem::setScaling(QVector3D scaling)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem10setScalingE9QVector3D(
    QCustom3DItem *self,
    const QVector3D *scaling) {
  self->setScaling(*scaling);
}

//  QVector3D QCustom3DItem::scaling() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK13QCustom3DItem7scalingEv(const QCustom3DItem *self) {
  return new QVector3D(self->scaling());
}

//  void QCustom3DItem::setScalingAbsolute(bool scalingAbsolute)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem18setScalingAbsoluteEb(
    QCustom3DItem *self,
    bool scalingAbsolute) {
  self->setScalingAbsolute(scalingAbsolute);
}

//  bool QCustom3DItem::isScalingAbsolute() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCustom3DItem17isScalingAbsoluteEv(
    const QCustom3DItem *self) {
  return self->isScalingAbsolute();
}

//  void QCustom3DItem::setRotation(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem11setRotationERK11QQuaternion(
    QCustom3DItem *self,
    const QQuaternion *rotation) {
  self->setRotation(*rotation);
}

//  QQuaternion QCustom3DItem::rotation()
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN13QCustom3DItem8rotationEv(QCustom3DItem *self) {
  return new QQuaternion(self->rotation());
}

//  void QCustom3DItem::setRotationAbsolute(bool rotationAbsolute)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem19setRotationAbsoluteEb(
    QCustom3DItem *self,
    bool rotationAbsolute) {
  self->setRotationAbsolute(rotationAbsolute);
}

//  bool QCustom3DItem::isRotationAbsolute() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCustom3DItem18isRotationAbsoluteEv(
    const QCustom3DItem *self) {
  return self->isRotationAbsolute();
}

//  void QCustom3DItem::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem10setVisibleEb(
    QCustom3DItem *self,
    bool visible) {
  self->setVisible(visible);
}

//  bool QCustom3DItem::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCustom3DItem9isVisibleEv(const QCustom3DItem *self) {
  return self->isVisible();
}

//  void QCustom3DItem::setShadowCasting(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem16setShadowCastingEb(
    QCustom3DItem *self,
    bool enabled) {
  self->setShadowCasting(enabled);
}

//  bool QCustom3DItem::isShadowCasting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCustom3DItem15isShadowCastingEv(
    const QCustom3DItem *self) {
  return self->isShadowCasting();
}

//  void QCustom3DItem::setRotationAxisAndAngle(QVector3D axis, float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem23setRotationAxisAndAngleE9QVector3Df(
    QCustom3DItem *self,
    const QVector3D *axis,
    float angle) {
  self->setRotationAxisAndAngle(*axis, angle);
}

//  void QCustom3DItem::setTextureImage(const QImage &textureImage)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem15setTextureImageERK6QImage(
    QCustom3DItem *self,
    const QImage *textureImage) {
  self->setTextureImage(*textureImage);
}

//  void QCustom3DItem::meshFileChanged(const QString &meshFile)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem15meshFileChangedERK7QString(
    QCustom3DItem *self,
    const QString *meshFile) {
  self->meshFileChanged(*meshFile);
}

//  void QCustom3DItem::textureFileChanged(const QString &textureFile)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem18textureFileChangedERK7QString(
    QCustom3DItem *self,
    const QString *textureFile) {
  self->textureFileChanged(*textureFile);
}

//  void QCustom3DItem::positionChanged(QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem15positionChangedE9QVector3D(
    QCustom3DItem *self,
    const QVector3D *position) {
  self->positionChanged(*position);
}

//  void QCustom3DItem::positionAbsoluteChanged(bool positionAbsolute)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem23positionAbsoluteChangedEb(
    QCustom3DItem *self,
    bool positionAbsolute) {
  self->positionAbsoluteChanged(positionAbsolute);
}

//  void QCustom3DItem::scalingChanged(QVector3D scaling)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem14scalingChangedE9QVector3D(
    QCustom3DItem *self,
    const QVector3D *scaling) {
  self->scalingChanged(*scaling);
}

//  void QCustom3DItem::rotationChanged(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem15rotationChangedERK11QQuaternion(
    QCustom3DItem *self,
    const QQuaternion *rotation) {
  self->rotationChanged(*rotation);
}

//  void QCustom3DItem::rotationAbsoluteChanged(bool newRotationAbsolute)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem23rotationAbsoluteChangedEb(
    QCustom3DItem *self,
    bool newRotationAbsolute) {
  self->rotationAbsoluteChanged(newRotationAbsolute);
}

//  void QCustom3DItem::visibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem14visibleChangedEb(
    QCustom3DItem *self,
    bool visible) {
  self->visibleChanged(visible);
}

//  void QCustom3DItem::shadowCastingChanged(bool shadowCasting)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem20shadowCastingChangedEb(
    QCustom3DItem *self,
    bool shadowCasting) {
  self->shadowCastingChanged(shadowCasting);
}

//  void QCustom3DItem::scalingAbsoluteChanged(bool scalingAbsolute)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem22scalingAbsoluteChangedEb(
    QCustom3DItem *self,
    bool scalingAbsolute) {
  self->scalingAbsoluteChanged(scalingAbsolute);
}

//  void QCustom3DItem::needUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustom3DItem10needUpdateEv(QCustom3DItem *self) {
  self->needUpdate();
}

//  QCustom3DItem::QCustom3DItem(QCustom3DItemPrivate &d, QObject *parent)
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZN13QCustom3DItemC1ER20QCustom3DItemPrivateP7QObject(
    QCustom3DItemPrivate *d,
    QObject *parent) {
  return new CuteQCustom3DItem(*d, parent);
}

//  a Python function taken by a CuteQCustom3DItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCustom3DItem(
    QCustom3DItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCustom3DItem *>(self)->take(key, call);
}

//  QList<QCustom3DItem *>::QList()
extern "C" Q_DECL_EXPORT
QList<QCustom3DItem *> *ritual_list_make_QCustom3DItem_ptr() {
  return new QList<QCustom3DItem *>();
}

//  void QList<QCustom3DItem *>::append(const QCustom3DItem * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCustom3DItem_ptr(
    QList<QCustom3DItem *> *self,
    QCustom3DItem *element) {
  self->append(element);
}

//  qsizetype QList<QCustom3DItem *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCustom3DItem_ptr(
    const QList<QCustom3DItem *> *self) {
  return self->size();
}

//  const QCustom3DItem * &QList<QCustom3DItem *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_list_at_QCustom3DItem_ptr(
    const QList<QCustom3DItem *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QCustom3DItem *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCustom3DItem_ptr(QList<QCustom3DItem *> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
