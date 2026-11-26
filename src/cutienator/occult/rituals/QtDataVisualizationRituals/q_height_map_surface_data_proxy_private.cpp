//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qheightmapsurfacedataproxy_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QHeightMapSurfaceDataProxyPrivate' is pasted in, cut from what the moc
//  of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 1 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qheightmapsurfacedataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/qsurfacedataproxy_p.h>
#include <QtDataVisualization/private/qsurface3dseries_p.h>
#include <QtDataVisualization/private/qabstract3daxis_p.h>
#include <QtDataVisualization/private/qheightmapsurfacedataproxy_p.h>
#include <QtDataVisualization/private/qabstractdataproxy_p.h>
#include <QtDataVisualization/private/qabstract3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 9, as local:qheightmapsurfacedataproxy.cpp:defaultMinValue
const float defaultMinValue = 0.0f;

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 10, as local:qheightmapsurfacedataproxy.cpp:defaultMaxValue
const float defaultMaxValue = 10.0f;

//  from QtDataVisualization__QHeightMapSurfaceDataProxyPrivate.cpp, line 1, as moc:QHeightMapSurfaceDataProxyPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN33QHeightMapSurfaceDataProxyPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QHeightMapSurfaceDataProxyPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN33QHeightMapSurfaceDataProxyPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QHeightMapSurfaceDataProxyPrivate"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QHeightMapSurfaceDataProxyPrivate, qt_meta_tag_ZN33QHeightMapSurfaceDataProxyPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QHeightMapSurfaceDataProxyPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QSurfaceDataProxyPrivate::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN33QHeightMapSurfaceDataProxyPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN33QHeightMapSurfaceDataProxyPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN33QHeightMapSurfaceDataProxyPrivateE_t>.metaTypes,
    nullptr
} };

void QHeightMapSurfaceDataProxyPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QHeightMapSurfaceDataProxyPrivate *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QHeightMapSurfaceDataProxyPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QHeightMapSurfaceDataProxyPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN33QHeightMapSurfaceDataProxyPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QSurfaceDataProxyPrivate::qt_metacast(_clname);
}

int QHeightMapSurfaceDataProxyPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QSurfaceDataProxyPrivate::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 636, as _ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    QAbstractDataProxyPrivate::setSeries(series);
    QSurface3DSeries *surfaceSeries = static_cast<QSurface3DSeries *>(series);
    emit qptr()->seriesChanged(surfaceSeries);
}

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 432, as _ZN33QHeightMapSurfaceDataProxyPrivateD0Ev
inline QHeightMapSurfaceDataProxyPrivate::~QHeightMapSurfaceDataProxyPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 500, as _ZN24QSurfaceDataProxyPrivate4qptrEv
inline QSurfaceDataProxy *QSurfaceDataProxyPrivate::qptr()
{
    return static_cast<QSurfaceDataProxy *>(q_ptr);
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 400, as _ZN24QSurfaceDataProxyPrivateD2Ev
inline QSurfaceDataProxyPrivate::~QSurfaceDataProxyPrivate()
{
    clearArray();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstractdataproxy.cpp, line 97, as _ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    q_ptr->setParent(series);
    m_series = series;
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 628, as _ZN24QSurfaceDataProxyPrivate10clearArrayEv
inline void QSurfaceDataProxyPrivate::clearArray()
{
    for (int i = 0; i < m_dataArray->size(); i++)
        clearRow(i);
    m_dataArray->clear();
    delete m_dataArray;
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstractdataproxy.cpp, line 93, as _ZN25QAbstractDataProxyPrivateD2Ev
inline QAbstractDataProxyPrivate::~QAbstractDataProxyPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 620, as _ZN24QSurfaceDataProxyPrivate8clearRowEi
inline void QSurfaceDataProxyPrivate::clearRow(int rowIndex)
{
    if (m_dataArray->at(rowIndex)) {
        delete m_dataArray->at(rowIndex);
        (*m_dataArray)[rowIndex] = 0;
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 441, as _ZN33QHeightMapSurfaceDataProxyPrivate14setValueRangesEffff
inline void QHeightMapSurfaceDataProxyPrivate::setValueRanges(float minX, float maxX,
                                                       float minZ, float maxZ)
{
    bool minXChanged = false;
    bool maxXChanged = false;
    bool minZChanged = false;
    bool maxZChanged = false;
    if (m_minXValue != minX) {
        m_minXValue = minX;
        minXChanged = true;
    }
    if (m_minZValue != minZ) {
        m_minZValue = minZ;
        minZChanged = true;
    }
    if (m_maxXValue != maxX || minX >= maxX) {
        if (minX >= maxX) {
            m_maxXValue = minX + 1.0f;
            qWarning() << "Warning: Tried to set invalid range for X value range."
                          " Range automatically adjusted to a valid one:"
                       << minX << "-" << maxX << "-->" << m_minXValue << "-" << m_maxXValue;
        } else {
            m_maxXValue = maxX;
        }
        maxXChanged = true;
    }
    if (m_maxZValue != maxZ || minZ >= maxZ) {
        if (minZ >= maxZ) {
            m_maxZValue = minZ + 1.0f;
            qWarning() << "Warning: Tried to set invalid range for Z value range."
                          " Range automatically adjusted to a valid one:"
                       << minZ << "-" << maxZ << "-->" << m_minZValue << "-" << m_maxZValue;
        } else {
            m_maxZValue = maxZ;
        }
        maxZChanged = true;
    }

    if (minXChanged)
        emit qptr()->minXValueChanged(m_minXValue);
    if (minZChanged)
        emit qptr()->minZValueChanged(m_minZValue);
    if (maxXChanged)
        emit qptr()->maxXValueChanged(m_maxXValue);
    if (maxZChanged)
        emit qptr()->maxZValueChanged(m_maxZValue);

    if ((minXChanged || minZChanged || maxXChanged || maxZChanged) && !m_resolveTimer.isActive())
        m_resolveTimer.start(0);
}

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 492, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMinXValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMinXValue(float min)
{
    if (min != m_minXValue) {
        bool maxChanged = false;
        if (min >= m_maxXValue) {
            float oldMax = m_maxXValue;
            m_maxXValue = min + 1.0f;
            qWarning() << "Warning: Tried to set minimum X to equal or larger than maximum X for"
                          " value range. Maximum automatically adjusted to a valid one:"
                       << oldMax <<  "-->" << m_maxXValue;
            maxChanged = true;
        }
        m_minXValue = min;
        emit qptr()->minXValueChanged(m_minXValue);
        if (maxChanged)
            emit qptr()->maxXValueChanged(m_maxXValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 514, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMaxXValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMaxXValue(float max)
{
    if (m_maxXValue != max) {
        bool minChanged = false;
        if (max <= m_minXValue) {
            float oldMin = m_minXValue;
            m_minXValue = max - 1.0f;
            qWarning() << "Warning: Tried to set maximum X to equal or smaller than minimum X for"
                          " value range. Minimum automatically adjusted to a valid one:"
                       << oldMin <<  "-->" << m_minXValue;
            minChanged = true;
        }
        m_maxXValue = max;
        emit qptr()->maxXValueChanged(m_maxXValue);
        if (minChanged)
            emit qptr()->minXValueChanged(m_minXValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 536, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMinZValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMinZValue(float min)
{
    if (min != m_minZValue) {
        bool maxChanged = false;
        if (min >= m_maxZValue) {
            float oldMax = m_maxZValue;
            m_maxZValue = min + 1.0f;
            qWarning() << "Warning: Tried to set minimum Z to equal or larger than maximum Z for"
                          " value range. Maximum automatically adjusted to a valid one:"
                       << oldMax <<  "-->" << m_maxZValue;
            maxChanged = true;
        }
        m_minZValue = min;
        emit qptr()->minZValueChanged(m_minZValue);
        if (maxChanged)
            emit qptr()->maxZValueChanged(m_maxZValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 558, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMaxZValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMaxZValue(float max)
{
    if (m_maxZValue != max) {
        bool minChanged = false;
        if (max <= m_minZValue) {
            float oldMin = m_minZValue;
            m_minZValue = max - 1.0f;
            qWarning() << "Warning: Tried to set maximum Z to equal or smaller than minimum Z for"
                          " value range. Minimum automatically adjusted to a valid one:"
                       << oldMin <<  "-->" << m_minZValue;
            minChanged = true;
        }
        m_maxZValue = max;
        emit qptr()->maxZValueChanged(m_maxZValue);
        if (minChanged)
            emit qptr()->minZValueChanged(m_minZValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 580, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMinYValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMinYValue(float min)
{
    if (m_minYValue != min) {
        bool maxChanged = false;
        if (min >= m_maxYValue) {
            float oldMax = m_maxYValue;
            m_maxYValue = min + 1.0f;
            qWarning() << "Warning: Tried to set minimum Y to equal or larger than maximum Y for"
                          " value range. Maximum automatically adjusted to a valid one:"
                       << oldMax <<  "-->" << m_maxYValue;
            maxChanged = true;
        }
        m_minYValue = min;
        emit qptr()->minYValueChanged(m_minYValue);
        if (maxChanged)
            emit qptr()->maxYValueChanged(m_maxYValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 602, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMaxYValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMaxYValue(float max)
{
    if (m_maxYValue != max) {
        bool minChanged = false;
        if (max <= m_minYValue) {
            float oldMin = m_minYValue;
            m_minYValue = max - 1.0f;
            qWarning() << "Warning: Tried to set maximum Y to equal or smaller than minimum Y for"
                          " value range. Minimum automatically adjusted to a valid one:"
                       << oldMin <<  "-->" << m_minYValue;
            minChanged = true;
        }
        m_maxYValue = max;
        emit qptr()->maxYValueChanged(m_maxYValue);
        if (minChanged)
            emit qptr()->minYValueChanged(m_minYValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 624, as _ZN33QHeightMapSurfaceDataProxyPrivate13setAutoScaleYEb
inline void QHeightMapSurfaceDataProxyPrivate::setAutoScaleY(bool enabled)
{
    if (enabled != m_autoScaleY) {
        m_autoScaleY = enabled;
        emit qptr()->autoScaleYChanged(m_autoScaleY);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 436, as _ZN33QHeightMapSurfaceDataProxyPrivate4qptrEv
inline QHeightMapSurfaceDataProxy *QHeightMapSurfaceDataProxyPrivate::qptr()
{
    return static_cast<QHeightMapSurfaceDataProxy *>(q_ptr);
}

//  from ../qtdatavis3d/src/datavisualization/data/qheightmapsurfacedataproxy.cpp, line 635, as _ZN33QHeightMapSurfaceDataProxyPrivate20handlePendingResolveEv
inline void QHeightMapSurfaceDataProxyPrivate::handlePendingResolve()
{
    QImage heightImage = m_heightMap;
    int bytesInChannel = 1;
    float yMul = 1.0f / UINT8_MAX;

    bool is16bit = (heightImage.format() == QImage::Format_RGBX64
                    || heightImage.format() == QImage::Format_RGBA64
                    || heightImage.format() == QImage::Format_RGBA64_Premultiplied
                    || heightImage.format() == QImage::Format_Grayscale16);

    // Convert to RGB32 to be sure we're reading the right bytes
    if (is16bit) {
        if (heightImage.format() != QImage::Format_RGBX64)
            heightImage = heightImage.convertToFormat(QImage::Format_RGBX64);

        bytesInChannel = 2;
        yMul = 1.0f / UINT16_MAX;
    } else if (heightImage.format() != QImage::Format_RGB32) {
        heightImage = heightImage.convertToFormat(QImage::Format_RGB32);
    }

    uchar *bits = heightImage.bits();

    int imageHeight = heightImage.height();
    int imageWidth = heightImage.width();
    int bitCount = imageWidth * 4 * (imageHeight - 1) * bytesInChannel;
    int widthBits = imageWidth * 4 * bytesInChannel;
    float height = 0;

    // Do not recreate array if dimensions have not changed
    QSurfaceDataArray *dataArray = m_dataArray;
    if (imageWidth != qptr()->columnCount() || imageHeight != dataArray->size()) {
        dataArray = new QSurfaceDataArray;
        dataArray->reserve(imageHeight);
        for (int i = 0; i < imageHeight; i++) {
            QSurfaceDataRow *newProxyRow = new QSurfaceDataRow(imageWidth);
            dataArray->append(newProxyRow);
        }
    }
    yMul *= m_maxYValue - m_minYValue;
    float xMul = (m_maxXValue - m_minXValue) / float(imageWidth - 1);
    float zMul = (m_maxZValue - m_minZValue) / float(imageHeight - 1);

    // Last row and column are explicitly set to max values, as relying
    // on multiplier can cause rounding errors, resulting in the value being
    // slightly over the specified maximum, which in turn can lead to it not
    // getting rendered.
    int lastRow = imageHeight - 1;
    int lastCol = imageWidth - 1;
    if (heightImage.isGrayscale()) {
        // Grayscale, it's enough to read Red byte
        for (int i = 0; i < imageHeight; i++, bitCount -= widthBits) {
            QSurfaceDataRow &newRow = *dataArray->at(i);
            float zVal;
            if (i == lastRow)
                zVal = m_maxZValue;
            else
                zVal = (float(i) * zMul) + m_minZValue;
            int j = 0;
            float yVal = 0;
            uchar *pixelptr;
            for (; j < lastCol; j++) {
                pixelptr  = (uchar *)(bits + bitCount + (j * 4 * bytesInChannel));
                if (!m_autoScaleY)
                    yVal = *pixelptr;
                else
                    yVal = float(*pixelptr) * yMul + m_minYValue;
                newRow[j].setPosition(QVector3D((float(j) * xMul) + m_minXValue,
                                                yVal,
                                                zVal));
            }
            newRow[j].setPosition(QVector3D(m_maxXValue,
                                            yVal,
                                            zVal));
        }
    } else {
        // Not grayscale, we'll need to calculate height from RGB
        for (int i = 0; i < imageHeight; i++, bitCount -= widthBits) {
            QSurfaceDataRow &newRow = *dataArray->at(i);
            float zVal;
            if (i == lastRow)
                zVal = m_maxZValue;
            else
                zVal = (float(i) * zMul) + m_minZValue;
            int j = 0;
            float yVal = 0;
            for (; j < lastCol; j++) {
                int nextpixel = j * 4 * bytesInChannel;
                uchar *pixelptr = (uchar *)(bits + bitCount + nextpixel);
                if (is16bit) {
                    height = float(*((ushort *)pixelptr))
                        + float(*(((ushort *)pixelptr) + 1))
                        + float(*(((ushort *)pixelptr) + 2));
                } else {
                    height = (float(*pixelptr)
                            + float(*(pixelptr + 1))
                            + float(*(pixelptr + 2)));
                }
                if (!m_autoScaleY)
                    yVal = height / 3.0f;
                else
                    yVal = (height / 3.0f * yMul) + m_minYValue;

                newRow[j].setPosition(QVector3D((float(j) * xMul) + m_minXValue,
                                                yVal,
                                                zVal));
            }
            newRow[j].setPosition(QVector3D(m_maxXValue,
                                            yVal,
                                            zVal));
        }
    }

    qptr()->resetArray(dataArray);
    emit qptr()->heightMapChanged(m_heightMap);
}
//  -----------------------------------------------------------------------

//  A QHeightMapSurfaceDataProxyPrivate that Python can take functions over in. Every QHeightMapSurfaceDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQHeightMapSurfaceDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHeightMapSurfaceDataProxyPrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHeightMapSurfaceDataProxyPrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightMapSurfaceDataProxyPrivateCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightMapSurfaceDataProxyPrivateCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightMapSurfaceDataProxyPrivateCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightMapSurfaceDataProxyPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightMapSurfaceDataProxyPrivateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHeightMapSurfaceDataProxyPrivate : public QHeightMapSurfaceDataProxyPrivate {
public:
  using QHeightMapSurfaceDataProxyPrivate::QHeightMapSurfaceDataProxyPrivate;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyPrivateCall0 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QSurfaceDataProxyPrivate::setSeries(series);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyPrivateCall1 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyPrivateCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyPrivateCall2 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyPrivateCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyPrivateCall3 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyPrivateCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyPrivateCall4 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyPrivateCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyPrivateCall5 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyPrivateCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyPrivateCall6 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyPrivateCall7 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyPrivateCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHeightMapSurfaceDataProxyPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK33QHeightMapSurfaceDataProxyPrivate10metaObjectEv(
    const QHeightMapSurfaceDataProxyPrivate *self) {
  return self->metaObject();
}

//  void *QHeightMapSurfaceDataProxyPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN33QHeightMapSurfaceDataProxyPrivate11qt_metacastEPKc(
    QHeightMapSurfaceDataProxyPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHeightMapSurfaceDataProxyPrivate::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN33QHeightMapSurfaceDataProxyPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QHeightMapSurfaceDataProxyPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHeightMapSurfaceDataProxyPrivate::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN33QHeightMapSurfaceDataProxyPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHeightMapSurfaceDataProxyPrivate::tr(s, c, n));
}

//  QHeightMapSurfaceDataProxyPrivate::~QHeightMapSurfaceDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivateD1Ev(
    QHeightMapSurfaceDataProxyPrivate *self) {
  delete self;
}

//  void QHeightMapSurfaceDataProxyPrivate::setValueRanges(float minX, float
//      maxX, float minZ, float maxZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate14setValueRangesEffff(
    QHeightMapSurfaceDataProxyPrivate *self,
    float minX,
    float maxX,
    float minZ,
    float maxZ) {
  self->setValueRanges(minX, maxX, minZ, maxZ);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMinXValue(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMinXValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float min) {
  self->setMinXValue(min);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMaxXValue(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMaxXValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float max) {
  self->setMaxXValue(max);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMinZValue(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMinZValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float min) {
  self->setMinZValue(min);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMaxZValue(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMaxZValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float max) {
  self->setMaxZValue(max);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMinYValue(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMinYValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float min) {
  self->setMinYValue(min);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMaxYValue(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMaxYValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float max) {
  self->setMaxYValue(max);
}

//  void QHeightMapSurfaceDataProxyPrivate::setAutoScaleY(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate13setAutoScaleYEb(
    QHeightMapSurfaceDataProxyPrivate *self,
    bool enabled) {
  self->setAutoScaleY(enabled);
}

//  QHeightMapSurfaceDataProxy *QHeightMapSurfaceDataProxyPrivate::qptr()
extern "C" Q_DECL_EXPORT
QHeightMapSurfaceDataProxy *ritual_ZN33QHeightMapSurfaceDataProxyPrivate4qptrEv(
    QHeightMapSurfaceDataProxyPrivate *self) {
  return self->qptr();
}

//  void QHeightMapSurfaceDataProxyPrivate::handlePendingResolve()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate20handlePendingResolveEv(
    QHeightMapSurfaceDataProxyPrivate *self) {
  self->handlePendingResolve();
}

//  a Python function taken by a CuteQHeightMapSurfaceDataProxyPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHeightMapSurfaceDataProxyPrivate(
    QHeightMapSurfaceDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHeightMapSurfaceDataProxyPrivate *>(self)->take(key, call);
}
