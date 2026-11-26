//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdrag_p_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickdrag_p_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickdrag_p.h>
#include <QtQuick/private/qquickdrag_p_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickevents_p_p.h>
#include <QtQuick/private/qquickitemchangelistener_p.h>
#include <QtQuick/private/qquickpixmap_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qmimedata.h>
#include <QtCore/qstringconverter.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/qevent.h>
#include <QtGui/qstylehints.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qimagewriter.h>
#ifdef Q_OS_ANDROID
#include <QtQuick/QQuickItemGrabResult>
#endif
#include <QtGui/qpa/qplatformdrag.h>
#include <QtGui/qdrag.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 74, as _ZN25QQuickDragAttachedPrivate17itemParentChangedEP10QQuickItemS1_
inline void QQuickDragAttachedPrivate::itemParentChanged(QQuickItem *, QQuickItem *)
{
    if (!active || dragRestarted)
        return;

    QQuickWindow *newWindow = attachedItem->window();

    if (window != newWindow)
        restartDrag();
    else if (window)
        updatePosition();
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 66, as _ZN25QQuickDragAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickDragAttachedPrivate::itemGeometryChanged(QQuickItem *, QQuickGeometryChange change,
                                                    const QRectF &)
{
    if (!change.positionChange() || !active || itemMoved)
        return;
    updatePosition();
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 87, as _ZN25QQuickDragAttachedPrivate14updatePositionEv
inline void QQuickDragAttachedPrivate::updatePosition()
{
    Q_Q(QQuickDragAttached);
    itemMoved = true;
    if (!eventQueued) {
        eventQueued = true;
        QCoreApplication::postEvent(q, new QEvent(QEvent::User));
    }
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 97, as _ZN25QQuickDragAttachedPrivate11restartDragEv
inline void QQuickDragAttachedPrivate::restartDrag()
{
    Q_Q(QQuickDragAttached);
    dragRestarted = true;
    if (!eventQueued) {
        eventQueued = true;
        QCoreApplication::postEvent(q, new QEvent(QEvent::User));
    }
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 107, as _ZN25QQuickDragAttachedPrivate17deliverEnterEventEv
inline void QQuickDragAttachedPrivate::deliverEnterEvent()
{
    dragRestarted = false;
    itemMoved = false;

    window = attachedItem->window();

    mimeData->m_source = source;
    if (!overrideActions)
        mimeData->m_supportedActions = supportedActions;
    mimeData->m_keys = keys;

    if (window) {
        QDragEnterEvent event(attachedItem->mapToScene(hotSpot), mimeData->m_supportedActions,
                              mimeData, Qt::NoButton, Qt::NoModifier);
        QQuickDropEventEx::setProposedAction(&event, proposedAction);
        deliverEvent(window, &event);
    }
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 127, as _ZN25QQuickDragAttachedPrivate16deliverMoveEventEv
inline void QQuickDragAttachedPrivate::deliverMoveEvent()
{
    Q_Q(QQuickDragAttached);

    itemMoved = false;
    if (window) {
        QDragMoveEvent event(attachedItem->mapToScene(hotSpot), mimeData->m_supportedActions,
                             mimeData, Qt::NoButton, Qt::NoModifier);
        QQuickDropEventEx::setProposedAction(&event, proposedAction);
        deliverEvent(window, &event);
        if (target != dragGrabber.target()) {
            target = dragGrabber.target();
            emit q->targetChanged();
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 144, as _ZN25QQuickDragAttachedPrivate17deliverLeaveEventEv
inline void QQuickDragAttachedPrivate::deliverLeaveEvent()
{
    if (window) {
        QDragLeaveEvent event;
        deliverEvent(window, &event);
        window = nullptr;
    }
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 153, as _ZN25QQuickDragAttachedPrivate12deliverEventEP12QQuickWindowP6QEvent
inline void QQuickDragAttachedPrivate::deliverEvent(QQuickWindow *window, QEvent *event)
{
    Q_ASSERT(!inEvent);
    inEvent = true;
    QQuickWindowPrivate::get(window)->deliveryAgentPrivate()->deliverDragEvent(&dragGrabber, event);
    inEvent = false;
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 588, as _ZN25QQuickDragAttachedPrivate5startE6QFlagsIN2Qt10DropActionEE
inline void QQuickDragAttachedPrivate::start(Qt::DropActions supportedActions)
{
    Q_Q(QQuickDragAttached);
    Q_ASSERT(!active);

    if (!mimeData)
        mimeData = new QQuickDragMimeData;
    if (!listening) {
        QQuickItemPrivate::get(attachedItem)->addItemChangeListener(
                this, QQuickItemPrivate::Geometry | QQuickItemPrivate::Parent);
        listening = true;
    }

    mimeData->m_supportedActions = supportedActions;
    active = true;
    itemMoved = false;
    dragRestarted = false;

    deliverEnterEvent();

    if (target != dragGrabber.target()) {
        target = dragGrabber.target();
        emit q->targetChanged();
    }

    emit q->activeChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 870, as _ZN25QQuickDragAttachedPrivate9startDragE6QFlagsIN2Qt10DropActionEE7QPixmap
inline Qt::DropAction QQuickDragAttachedPrivate::startDrag(Qt::DropActions supportedActions,
                                                    QPixmap pixmap)
{
    Q_Q(QQuickDragAttached);

    QDrag *drag = new QDrag(source ? source : q);

    drag->setMimeData(createMimeData());
    if (!pixmap.isNull())
        drag->setPixmap(pixmap);
    else if (pixmapLoader.isReady())
        drag->setPixmap(QPixmap::fromImage(pixmapLoader.image()));

    drag->setHotSpot(hotSpot.toPoint());
    emit q->dragStarted();

    executingNativeDrag = true;
    Qt::DropAction dropAction = drag->exec(supportedActions);
    executingNativeDrag = false;

    if (!QGuiApplicationPrivate::platformIntegration()->drag()->ownsDragObject())
        drag->deleteLater();

    deliverLeaveEvent();

    if (target) {
        target = nullptr;
        emit q->targetChanged();
    }

    emit q->dragFinished(dropAction);

    active = false;
    emit q->activeChanged();

    return dropAction;
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 756, as _ZNK25QQuickDragAttachedPrivate14createMimeDataEv
inline QMimeData *QQuickDragAttachedPrivate::createMimeData() const
{
    Q_Q(const QQuickDragAttached);
    QMimeData *mimeData = new QMimeData();

    for (const auto [mimeType, value] : externalMimeData.asKeyValueRange()) {
        switch (value.typeId()) {
        case QMetaType::QByteArray:
            // byte array assumed to already be correctly encoded
            mimeData->setData(mimeType, value.toByteArray());
            break;
        case QMetaType::QString: {
            const QString text = value.toString();
            if (mimeType == u"text/plain"_s) {
                mimeData->setText(text);
            } else if (mimeType == u"text/html"_s) {
                mimeData->setHtml(text);
            } else if (mimeType == u"text/uri-list"_s) {
                QList<QUrl> urls;
                // parse and split according to RFC2483
                const auto lines = text.split(u"\r\n"_s, Qt::SkipEmptyParts);
                for (const auto &line : lines) {
                    const QUrl url(line);
                    if (url.isValid())
                        urls.push_back(url);
                    else
                        qmlWarning(q) << line << " is not a valid URI";

                }
                mimeData->setUrls(urls);
            } else if (mimeType.startsWith(u"text/"_s)) {
                if (qsizetype charsetIdx = mimeType.lastIndexOf(u";charset="_s); charsetIdx != -1) {
                    charsetIdx += sizeof(";charset=") - 1;
                    const QByteArray encoding = mimeType.mid(charsetIdx).toUtf8();
                    QStringEncoder encoder(encoding);
                    if (encoder.isValid())
                        mimeData->setData(mimeType, encoder.encode(text));
                    else
                        qmlWarning(q) << "Don't know how to encode text as " << mimeType;
                } else {
                    mimeData->setData(mimeType, text.toUtf8());
                }
            } else {
                mimeData->setData(mimeType, text.toUtf8());
            }
            break;
        }
        case QMetaType::QVariantList:
        case QMetaType::QStringList:
            if (mimeType == u"text/uri-list"_s) {
                const QVariantList values = value.toList();
                QList<QUrl> urls;
                urls.reserve(values.size());
                bool error = false;
                for (qsizetype index = 0; index < values.size(); ++index) {
                    const QUrl url = values.at(index).value<QUrl>();
                    if (url.isValid()) {
                        urls += url;
                    } else {
                        error = true;
                        qmlWarning(q) << "Value '" << values.at(index) << "' at index " << index
                                      << " is not a valid URI";
                    }
                }
                if (!error)
                    mimeData->setUrls(urls);
            }
            break;
        case QMetaType::QColor:
            if (mimeType == u"application/x-color"_s)
                mimeData->setColorData(value);
            break;
        case QMetaType::QImage:
            if (const QByteArray mimeTypeUtf8 = mimeType.toUtf8();
                QImageWriter::supportedMimeTypes().contains(mimeTypeUtf8)) {
                const auto imageFormats = QImageWriter::imageFormatsForMimeType(mimeTypeUtf8);
                if (imageFormats.isEmpty()) { // shouldn't happen, but we can fall back
                    mimeData->setImageData(value);
                    break;
                }
                const QImage image = value.value<QImage>();
                QByteArray bytes;
                {
                    QBuffer buffer(&bytes);
                    QImageWriter encoder(&buffer, imageFormats.first());
                    encoder.write(image);
                }
                mimeData->setData(mimeType, bytes);
                break;
            }
            Q_FALLTHROUGH();
        default:
            qmlWarning(q) << "Don't know how to encode variant of type " << value.metaType()
                          << " as mime type " << mimeType;
            // compatibility with pre-6.5 - probably a bad idea
            mimeData->setData(mimeType, value.toString().toUtf8());
            break;
        }
    }

    return mimeData;
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 859, as _ZN25QQuickDragAttachedPrivate10loadPixmapEv
inline void QQuickDragAttachedPrivate::loadPixmap()
{
    Q_Q(QQuickDragAttached);

    QUrl loadUrl = imageSource;
    const QQmlContext *context = qmlContext(q->parent());
    if (context)
        loadUrl = context->resolvedUrl(imageSource);
    pixmapLoader.load(context ? context->engine() : nullptr, loadUrl, QRect(), q->imageSourceSize());
}
//  -----------------------------------------------------------------------

//  A QQuickDragAttachedPrivate that Python can take functions over in. Every QQuickDragAttachedPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickDragAttachedPrivateCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickDragAttachedPrivateCall1)(const void *, QQuickItem *, QQuickItem *, int *);
class CuteQQuickDragAttachedPrivate : public QQuickDragAttachedPrivate {
public:
  using QQuickDragAttachedPrivate::QQuickDragAttachedPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QQuickDragAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QQuickDragAttachedPrivate17itemParentChangedEP10QQuickItemS1_")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QQuickDragAttachedPrivate::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDragAttachedPrivateCall0 call = reinterpret_cast<CuteQQuickDragAttachedPrivateCall0>(taken[0]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickDragAttachedPrivate::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickDragAttachedPrivate::itemParentChanged(QQuickItem *a0,
  //      QQuickItem *parent)
  void itemParentChanged(QQuickItem *a0, QQuickItem *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDragAttachedPrivateCall1 call = reinterpret_cast<CuteQQuickDragAttachedPrivateCall1>(taken[1]);
      call(this, a0, parent, &handled);
      if (handled) return;
    }
    QQuickDragAttachedPrivate::itemParentChanged(a0, parent);
  }
};

//  QQuickDragAttached *QQuickDragAttachedPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickDragAttached *ritual_ZN25QQuickDragAttachedPrivate6q_funcEv(
    QQuickDragAttachedPrivate *self) {
  return self->q_func();
}

//  const QQuickDragAttached *QQuickDragAttachedPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickDragAttached *ritual_ZNK25QQuickDragAttachedPrivate6q_funcEv(
    const QQuickDragAttachedPrivate *self) {
  return self->q_func();
}

//  void QQuickDragAttachedPrivate::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate22qt_qmlMarker_anonymousEv(
    QQuickDragAttachedPrivate *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickDragAttachedPrivate
//      *QQuickDragAttachedPrivate::get(QQuickDragAttached *attached)
extern "C" Q_DECL_EXPORT
QQuickDragAttachedPrivate *ritual_ZN25QQuickDragAttachedPrivate3getEP18QQuickDragAttached(
    QQuickDragAttached *attached) {
  return QQuickDragAttachedPrivate::get(attached);
}

//  QQuickDragAttachedPrivate::QQuickDragAttachedPrivate()
extern "C" Q_DECL_EXPORT
QQuickDragAttachedPrivate *ritual_ZN25QQuickDragAttachedPrivateC1Ev() {
  return new CuteQQuickDragAttachedPrivate();
}

//  void QQuickDragAttachedPrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickDragAttachedPrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickDragAttachedPrivate::itemParentChanged(QQuickItem *a0,
//      QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate17itemParentChangedEP10QQuickItemS1_(
    QQuickDragAttachedPrivate *self,
    QQuickItem *a0,
    QQuickItem *parent) {
  self->itemParentChanged(a0, parent);
}

//  void QQuickDragAttachedPrivate::updatePosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate14updatePositionEv(
    QQuickDragAttachedPrivate *self) {
  self->updatePosition();
}

//  void QQuickDragAttachedPrivate::restartDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate11restartDragEv(
    QQuickDragAttachedPrivate *self) {
  self->restartDrag();
}

//  void QQuickDragAttachedPrivate::deliverEnterEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate17deliverEnterEventEv(
    QQuickDragAttachedPrivate *self) {
  self->deliverEnterEvent();
}

//  void QQuickDragAttachedPrivate::deliverMoveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate16deliverMoveEventEv(
    QQuickDragAttachedPrivate *self) {
  self->deliverMoveEvent();
}

//  void QQuickDragAttachedPrivate::deliverLeaveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate17deliverLeaveEventEv(
    QQuickDragAttachedPrivate *self) {
  self->deliverLeaveEvent();
}

//  void QQuickDragAttachedPrivate::deliverEvent(QQuickWindow *window, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate12deliverEventEP12QQuickWindowP6QEvent(
    QQuickDragAttachedPrivate *self,
    QQuickWindow *window,
    QEvent *event) {
  self->deliverEvent(window, event);
}

//  void QQuickDragAttachedPrivate::start(Qt::DropActions supportedActions)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate5startE6QFlagsIN2Qt10DropActionEE(
    QQuickDragAttachedPrivate *self,
    int supportedActions) {
  self->start(QFlags<Qt::DropAction>::fromInt(supportedActions));
}

//  Qt::DropAction QQuickDragAttachedPrivate::startDrag(Qt::DropActions
//      supportedActions, QPixmap pixmap)
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZN25QQuickDragAttachedPrivate9startDragE6QFlagsIN2Qt10DropActionEE7QPixmap(
    QQuickDragAttachedPrivate *self,
    int supportedActions,
    const QPixmap *pixmap) {
  return self->startDrag(
      QFlags<Qt::DropAction>::fromInt(supportedActions),
      *pixmap);
}

//  QMimeData *QQuickDragAttachedPrivate::createMimeData() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK25QQuickDragAttachedPrivate14createMimeDataEv(
    const QQuickDragAttachedPrivate *self) {
  return self->createMimeData();
}

//  void QQuickDragAttachedPrivate::loadPixmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate10loadPixmapEv(
    QQuickDragAttachedPrivate *self) {
  self->loadPixmap();
}

//  a Python function taken by a CuteQQuickDragAttachedPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDragAttachedPrivate(
    QQuickDragAttachedPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDragAttachedPrivate *>(self)->take(key, call);
}

//  void QQuickDragAttachedPrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickDragAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickDragAttachedPrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->QQuickDragAttachedPrivate::itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickDragAttachedPrivate::itemParentChanged(QQuickItem *a0,
//      QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickDragAttachedPrivate17itemParentChangedEP10QQuickItemS1_(
    QQuickDragAttachedPrivate *self,
    QQuickItem *a0,
    QQuickItem *parent) {
  self->QQuickDragAttachedPrivate::itemParentChanged(a0, parent);
}

#endif  // QT_CONFIG(quick_draganddrop)
