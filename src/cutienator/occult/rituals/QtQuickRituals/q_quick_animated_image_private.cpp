//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimatedimage_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_animatedimage)
#if QT_CONFIG(quick_animatedimage)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_animatedimage)
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatedimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatedimage_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickanimatedimage_p.h>
#include <QtQuick/private/qquickanimatedimage_p_p.h>
#include <QtGui/qguiapplication.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlfile.h>
#include <QtQml/qqmlengine.h>
#include <QtGui/qmovie.h>
#if QT_CONFIG(qml_network)
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/qnetworkreply.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickanimatedimage.cpp, line 20, as _ZN26QQuickAnimatedImagePrivate19infoForCurrentFrameEP10QQmlEngine
inline QQuickPixmap* QQuickAnimatedImagePrivate::infoForCurrentFrame(QQmlEngine *engine)
{
    if (!movie)
        return nullptr;

    int current = movie->currentFrameNumber();
    if (!frameMap.contains(current)) {
        QUrl requestedUrl;
        QQuickPixmap *pixmap = nullptr;
        if (engine && !movie->fileName().isEmpty()) {
            requestedUrl.setUrl(QString::fromUtf8("quickanimatedimage://%1#%2x%3#%4")
                                .arg(movie->fileName())
                                .arg(movie->scaledSize().width())
                                .arg(movie->scaledSize().height())
                                .arg(current));
        }
        if (!requestedUrl.isEmpty()) {
            if (QQuickPixmap::isCached(requestedUrl, QRect(), QSize(), 0, QQuickImageProviderOptions()))
                pixmap = new QQuickPixmap(engine, requestedUrl);
            else
                pixmap = new QQuickPixmap(requestedUrl, movie->currentImage());
        } else {
            pixmap = new QQuickPixmap;
            pixmap->setImage(movie->currentImage());
        }
        frameMap.insert(current, pixmap);
    }

    return frameMap.value(current);
}

//  from ../qtdeclarative/src/quick/items/qquickanimatedimage.cpp, line 623, as _ZN26QQuickAnimatedImagePrivate8setMovieEP6QMovie
inline void QQuickAnimatedImagePrivate::setMovie(QMovie *m)
{
    if (movie == m)
        return;

    Q_Q(QQuickAnimatedImage);
    const int oldFrameCount = q->frameCount();

    if (movie) {
        movie->disconnect();
        movie->deleteLater();
    }

    movie = m;
    clearCache();

    if (movie)
        movie->setScaledSize(sourcesize);

    if (oldFrameCount != q->frameCount())
        emit q->frameCountChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickanimatedimage.cpp, line 51, as _ZN26QQuickAnimatedImagePrivate10clearCacheEv
inline void QQuickAnimatedImagePrivate::clearCache()
{
    qDeleteAll(frameMap);
    frameMap.clear();
}

//  from ../qtdeclarative/src/quick/items/qquickanimatedimage.cpp, line 57, as _ZN26QQuickAnimatedImagePrivate20handleLoopCompletionEv
inline void QQuickAnimatedImagePrivate::handleLoopCompletion()
{
    Q_Q(QQuickAnimatedImage);
    const int targetFrame = (finishBehavior == QQuickAnimatedImage::FinishAtInitialFrame)
                            ? 0
                            : qMax(movie->frameCount() - 1, 0);
    lastFrameNumber = targetFrame;
    movie->stop();
    movie->jumpToFrame(targetFrame);
    // playing = false will be set via playingStatusChanged()
    emit q->finished();
}
//  -----------------------------------------------------------------------

//  A QQuickAnimatedImagePrivate that Python can take functions over in. Every QQuickAnimatedImagePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickAnimatedImagePrivateCall0)(const void *, qreal, int *);
typedef void (*CuteQQuickAnimatedImagePrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickAnimatedImagePrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickAnimatedImagePrivateCall3)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickAnimatedImagePrivateCall4)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickAnimatedImagePrivateCall5)(const void *, int, int *);
typedef qreal (*CuteQQuickAnimatedImagePrivateCall6)(const void *, int *);
typedef qreal (*CuteQQuickAnimatedImagePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickAnimatedImagePrivateCall8)(const void *, int *);
typedef void (*CuteQQuickAnimatedImagePrivateCall9)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickAnimatedImagePrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickAnimatedImagePrivateCall11)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickAnimatedImagePrivateCall12)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickAnimatedImagePrivateCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickAnimatedImagePrivateCall14)(const void *, bool, int *);
typedef void * (*CuteQQuickAnimatedImagePrivateCall15)(const void *, int *);
typedef void (*CuteQQuickAnimatedImagePrivateCall16)(const void *, int *);
typedef void (*CuteQQuickAnimatedImagePrivateCall17)(const void *, int *);
typedef void (*CuteQQuickAnimatedImagePrivateCall18)(const void *, int, int *);
class CuteQQuickAnimatedImagePrivate : public QQuickAnimatedImagePrivate {
public:
  using QQuickAnimatedImagePrivate::QQuickAnimatedImagePrivate;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickImageBasePrivate22updateDevicePixelRatioEd")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[12] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

  //  bool QQuickImageBasePrivate::updateDevicePixelRatio(qreal
  //      targetDevicePixelRatio)
  bool updateDevicePixelRatio(qreal targetDevicePixelRatio) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall0 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall0>(taken[0]);
      bool given = call(this, targetDevicePixelRatio, &handled);
      if (handled) return given;
    }
    return QQuickImageBasePrivate::updateDevicePixelRatio(targetDevicePixelRatio);
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall1 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall1>(taken[1]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall2 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall2>(taken[2]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall3 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall3>(taken[3]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall4 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall4>(taken[4]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall5 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall5>(taken[5]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall6 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall7 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall7>(taken[7]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall8 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall9 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall10 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall11 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall11>(taken[11]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall12 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall12>(taken[12]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall13 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall13>(taken[13]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall14 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall14>(taken[14]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall15 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall16 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall17 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickAnimatedImagePrivateCall18 call = reinterpret_cast<CuteQQuickAnimatedImagePrivateCall18>(taken[18]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickAnimatedImage *QQuickAnimatedImagePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickAnimatedImage *ritual_ZN26QQuickAnimatedImagePrivate6q_funcEv(
    QQuickAnimatedImagePrivate *self) {
  return self->q_func();
}

//  const QQuickAnimatedImage *QQuickAnimatedImagePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickAnimatedImage *ritual_ZNK26QQuickAnimatedImagePrivate6q_funcEv(
    const QQuickAnimatedImagePrivate *self) {
  return self->q_func();
}

//  QQuickAnimatedImagePrivate::QQuickAnimatedImagePrivate()
extern "C" Q_DECL_EXPORT
QQuickAnimatedImagePrivate *ritual_ZN26QQuickAnimatedImagePrivateC1Ev() {
  return new CuteQQuickAnimatedImagePrivate();
}

//  QQuickPixmap *QQuickAnimatedImagePrivate::infoForCurrentFrame(QQmlEngine
//      *engine)
extern "C" Q_DECL_EXPORT
QQuickPixmap *ritual_ZN26QQuickAnimatedImagePrivate19infoForCurrentFrameEP10QQmlEngine(
    QQuickAnimatedImagePrivate *self,
    QQmlEngine *engine) {
  return self->infoForCurrentFrame(engine);
}

//  void QQuickAnimatedImagePrivate::setMovie(QMovie *movie)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAnimatedImagePrivate8setMovieEP6QMovie(
    QQuickAnimatedImagePrivate *self,
    QMovie *movie) {
  self->setMovie(movie);
}

//  void QQuickAnimatedImagePrivate::clearCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAnimatedImagePrivate10clearCacheEv(
    QQuickAnimatedImagePrivate *self) {
  self->clearCache();
}

//  void QQuickAnimatedImagePrivate::handleLoopCompletion()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAnimatedImagePrivate20handleLoopCompletionEv(
    QQuickAnimatedImagePrivate *self) {
  self->handleLoopCompletion();
}

//  a Python function taken by a CuteQQuickAnimatedImagePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnimatedImagePrivate(
    QQuickAnimatedImagePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnimatedImagePrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_animatedimage)
#endif  // QT_CONFIG(quick_animatedimage)
