//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qcustom3dvolume_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qcustom3dvolume_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/qcustom3ditem_p.h>
#include <QtDataVisualization/private/qcustom3dvolume_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/qquaternion.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 460, as _ZN20QCustom3DItemPrivateC2EP13QCustom3DItem
inline QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItem *q) :
    q_ptr(q),
    m_textureImage(QImage(1, 1, QImage::Format_ARGB32)),
    m_position(QVector3D(0.0f, 0.0f, 0.0f)),
    m_positionAbsolute(false),
    m_scaling(QVector3D(0.1f, 0.1f, 0.1f)),
    m_scalingAbsolute(true),
    m_rotation(identityQuaternion),
    m_visible(true),
    m_shadowCasting(true),
    m_isLabelItem(false),
    m_isVolumeItem(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 493, as _ZN20QCustom3DItemPrivateD2Ev
inline QCustom3DItemPrivate::~QCustom3DItemPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 508, as _ZN20QCustom3DItemPrivate14resetDirtyBitsEv
inline void QCustom3DItemPrivate::resetDirtyBits()
{
    m_dirtyBits.textureDirty = false;
    m_dirtyBits.meshDirty = false;
    m_dirtyBits.positionDirty = false;
    m_dirtyBits.scalingDirty = false;
    m_dirtyBits.rotationDirty = false;
    m_dirtyBits.visibleDirty = false;
    m_dirtyBits.shadowCastingDirty = false;
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3dvolume.cpp, line 1203, as _ZN22QCustom3DVolumePrivate14resetDirtyBitsEv
inline void QCustom3DVolumePrivate::resetDirtyBits()
{
    QCustom3DItemPrivate::resetDirtyBits();

    m_dirtyBitsVolume.textureDimensionsDirty = false;
    m_dirtyBitsVolume.slicesDirty = false;
    m_dirtyBitsVolume.colorTableDirty = false;
    m_dirtyBitsVolume.textureDataDirty = false;
    m_dirtyBitsVolume.textureFormatDirty = false;
    m_dirtyBitsVolume.alphaDirty = false;
    m_dirtyBitsVolume.shaderDirty = false;
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3dvolume.cpp, line 1216, as _ZN22QCustom3DVolumePrivate11renderSliceEN2Qt4AxisEi
inline QImage QCustom3DVolumePrivate::renderSlice(Qt::Axis axis, int index)
{
    if (index < 0)
        return QImage();

    int x;
    int y;
    if (axis == Qt::XAxis) {
        if (index >= m_textureWidth)
            return QImage();
        x = m_textureDepth;
        y = m_textureHeight;
    } else if (axis == Qt::YAxis) {
        if (index >= m_textureHeight)
            return QImage();
        x = m_textureWidth;
        y = m_textureDepth;
    } else {
        if (index >= m_textureDepth)
            return QImage();
        x = m_textureWidth;
        y = m_textureHeight;
    }

    int padding = 0;
    int pixelWidth = 4;
    int dataWidth = qptr()->textureDataWidth();
    if (m_textureFormat == QImage::Format_Indexed8) {
        padding = x % 4;
        pixelWidth = 1;
    }
    QList<uchar> data((x + padding) * y * pixelWidth);
    int frameSize = qptr()->textureDataWidth() * m_textureHeight;

    int dataIndex = 0;
    if (axis == Qt::XAxis) {
        for (int i = 0; i < y; i++) {
            const uchar *p = m_textureData->constData()
                    + (index * pixelWidth) + (dataWidth * i);
            for (int j = 0; j < x; j++) {
                for (int k = 0; k < pixelWidth; k++)
                    data[dataIndex++] = *(p + k);
                p += frameSize;
            }
        }
    } else if (axis == Qt::YAxis) {
        for (int i = y - 1; i >= 0; i--) {
            const uchar *p = m_textureData->constData() + (index * dataWidth)
                    + (frameSize * i);
            for (int j = 0; j < (x * pixelWidth); j++) {
                data[dataIndex++] = *p;
                p++;
            }
        }
    } else {
        for (int i = 0; i < y; i++) {
            const uchar *p = m_textureData->constData() + (index * frameSize) + (dataWidth * i);
            for (int j = 0; j < (x * pixelWidth); j++) {
                data[dataIndex++] = *p;
                p++;
            }
        }
    }

    if (m_textureFormat != QImage::Format_Indexed8 && m_alphaMultiplier != 1.0f) {
        for (int i = pixelWidth - 1; i < data.size(); i += pixelWidth)
            data[i] = static_cast<uchar>(multipliedAlphaValue(data.at(i)));
    }

    return [&] {
    QImage image(data.constData(), x, y, x * pixelWidth, m_textureFormat);
    image.bits(); // Call bits() to detach the new image from local data
    if (m_textureFormat == QImage::Format_Indexed8) {
        QList<QRgb> colorTable = m_colorTable;
        if (m_alphaMultiplier != 1.0f) {
            for (int i = 0; i < colorTable.size(); i++) {
                QRgb curCol = colorTable.at(i);
                int alpha = multipliedAlphaValue(qAlpha(curCol));
                if (alpha != qAlpha(curCol))
                    colorTable[i] = qRgba(qRed(curCol), qGreen(curCol), qBlue(curCol), alpha);
            }
        }
        image.setColorTable(colorTable);
    }

    return image;
    }();
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3dvolume.cpp, line 1315, as _ZN22QCustom3DVolumePrivate4qptrEv
inline QCustom3DVolume *QCustom3DVolumePrivate::qptr()
{
    return static_cast<QCustom3DVolume *>(q_ptr);
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3dvolume.cpp, line 1305, as _ZN22QCustom3DVolumePrivate20multipliedAlphaValueEi
inline int QCustom3DVolumePrivate::multipliedAlphaValue(int alpha)
{
    int modifiedAlpha = alpha;
    if (!m_preserveOpacity || alpha != 255) {
        modifiedAlpha = int(m_alphaMultiplier * float(alpha));
        modifiedAlpha = qMin(modifiedAlpha, 255);
    }
    return modifiedAlpha;
}
//  -----------------------------------------------------------------------

//  A QCustom3DVolumePrivate that Python can take functions over in. Every QCustom3DVolumePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DVolumePrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DVolumePrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DVolumePrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DVolumePrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DVolumePrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DVolumePrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DVolumePrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCustom3DVolumePrivate : public QCustom3DVolumePrivate {
public:
  using QCustom3DVolumePrivate::QCustom3DVolumePrivate;
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
      CuteQCustom3DVolumePrivateCall0 call = reinterpret_cast<CuteQCustom3DVolumePrivateCall0>(taken[0]);
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
      CuteQCustom3DVolumePrivateCall1 call = reinterpret_cast<CuteQCustom3DVolumePrivateCall1>(taken[1]);
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
      CuteQCustom3DVolumePrivateCall2 call = reinterpret_cast<CuteQCustom3DVolumePrivateCall2>(taken[2]);
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
      CuteQCustom3DVolumePrivateCall3 call = reinterpret_cast<CuteQCustom3DVolumePrivateCall3>(taken[3]);
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
      CuteQCustom3DVolumePrivateCall4 call = reinterpret_cast<CuteQCustom3DVolumePrivateCall4>(taken[4]);
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
      CuteQCustom3DVolumePrivateCall5 call = reinterpret_cast<CuteQCustom3DVolumePrivateCall5>(taken[5]);
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
      CuteQCustom3DVolumePrivateCall6 call = reinterpret_cast<CuteQCustom3DVolumePrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCustom3DVolumePrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QCustom3DVolumePrivate10metaObjectEv(
    const QCustom3DVolumePrivate *self) {
  return self->metaObject();
}

//  QCustom3DVolumePrivate::~QCustom3DVolumePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCustom3DVolumePrivateD1Ev(QCustom3DVolumePrivate *self) {
  delete self;
}

//  void QCustom3DVolumePrivate::resetDirtyBits()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCustom3DVolumePrivate14resetDirtyBitsEv(
    QCustom3DVolumePrivate *self) {
  self->resetDirtyBits();
}

//  QImage QCustom3DVolumePrivate::renderSlice(Qt::Axis axis, int index)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN22QCustom3DVolumePrivate11renderSliceEN2Qt4AxisEi(
    QCustom3DVolumePrivate *self,
    Qt::Axis axis,
    int index) {
  return new QImage(self->renderSlice(axis, index));
}

//  QCustom3DVolume *QCustom3DVolumePrivate::qptr()
extern "C" Q_DECL_EXPORT
QCustom3DVolume *ritual_ZN22QCustom3DVolumePrivate4qptrEv(
    QCustom3DVolumePrivate *self) {
  return self->qptr();
}

//  int QCustom3DVolumePrivate::multipliedAlphaValue(int alpha)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QCustom3DVolumePrivate20multipliedAlphaValueEi(
    QCustom3DVolumePrivate *self,
    int alpha) {
  return self->multipliedAlphaValue(alpha);
}

//  a Python function taken by a CuteQCustom3DVolumePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCustom3DVolumePrivate(
    QCustom3DVolumePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCustom3DVolumePrivate *>(self)->take(key, call);
}
