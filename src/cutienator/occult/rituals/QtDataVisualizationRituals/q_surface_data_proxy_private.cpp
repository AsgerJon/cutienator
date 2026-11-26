//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qsurfacedataproxy_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QSurfaceDataProxyPrivate'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 2 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qsurfacedataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDataVisualization/qsurfacedataitem.h>
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
#include <QtDataVisualization/private/qabstractdataproxy_p.h>
#include <QtDataVisualization/private/qabstract3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__QSurfaceDataProxyPrivate.cpp, line 1, as moc:QSurfaceDataProxyPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN24QSurfaceDataProxyPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QSurfaceDataProxyPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN24QSurfaceDataProxyPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSurfaceDataProxyPrivate"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QSurfaceDataProxyPrivate, qt_meta_tag_ZN24QSurfaceDataProxyPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSurfaceDataProxyPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstractDataProxyPrivate::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QSurfaceDataProxyPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QSurfaceDataProxyPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN24QSurfaceDataProxyPrivateE_t>.metaTypes,
    nullptr
} };

void QSurfaceDataProxyPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QSurfaceDataProxyPrivate *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QSurfaceDataProxyPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSurfaceDataProxyPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QSurfaceDataProxyPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QAbstractDataProxyPrivate::qt_metacast(_clname);
}

int QSurfaceDataProxyPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractDataProxyPrivate::qt_metacall(_c, _id, _a);
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

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 400, as _ZN24QSurfaceDataProxyPrivateD0Ev
inline QSurfaceDataProxyPrivate::~QSurfaceDataProxyPrivate()
{
    clearArray();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstractdataproxy.cpp, line 84, as _ZN25QAbstractDataProxyPrivateC2EP18QAbstractDataProxyNS0_8DataTypeE
inline QAbstractDataProxyPrivate::QAbstractDataProxyPrivate(QAbstractDataProxy *q,
                                                     QAbstractDataProxy::DataType type)
    : QObject(0),
      q_ptr(q),
      m_type(type),
      m_series(0)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstractdataproxy.cpp, line 93, as _ZN25QAbstractDataProxyPrivateD2Ev
inline QAbstractDataProxyPrivate::~QAbstractDataProxyPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstractdataproxy.cpp, line 97, as _ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    q_ptr->setParent(series);
    m_series = series;
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 394, as _ZN24QSurfaceDataProxyPrivateC1EP17QSurfaceDataProxy
inline QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate(QSurfaceDataProxy *q)
    : QAbstractDataProxyPrivate(q, QAbstractDataProxy::DataTypeSurface),
      m_dataArray(new QSurfaceDataArray)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 405, as _ZN24QSurfaceDataProxyPrivate10resetArrayEP5QListIPS0_I16QSurfaceDataItemEE
inline void QSurfaceDataProxyPrivate::resetArray(QSurfaceDataArray *newArray)
{
    if (!newArray)
        newArray = new QSurfaceDataArray;

    if (newArray != m_dataArray) {
        clearArray();
        m_dataArray = newArray;
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 416, as _ZN24QSurfaceDataProxyPrivate6setRowEiP5QListI16QSurfaceDataItemE
inline void QSurfaceDataProxyPrivate::setRow(int rowIndex, QSurfaceDataRow *row)
{
    Q_ASSERT(rowIndex >= 0 && rowIndex < m_dataArray->size());
    Q_ASSERT(m_dataArray->at(rowIndex)->size() == row->size());

    if (row != m_dataArray->at(rowIndex)) {
        clearRow(rowIndex);
        (*m_dataArray)[rowIndex] = row;
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 427, as _ZN24QSurfaceDataProxyPrivate7setRowsEiRK5QListIPS0_I16QSurfaceDataItemEE
inline void QSurfaceDataProxyPrivate::setRows(int rowIndex, const QSurfaceDataArray &rows)
{
    QSurfaceDataArray &dataArray = *m_dataArray;
    Q_ASSERT(rowIndex >= 0 && (rowIndex + rows.size()) <= dataArray.size());

    for (int i = 0; i < rows.size(); i++) {
        Q_ASSERT(m_dataArray->at(rowIndex)->size() == rows.at(i)->size());
        if (rows.at(i) != dataArray.at(rowIndex)) {
            clearRow(rowIndex);
            dataArray[rowIndex] = rows.at(i);
        }
        rowIndex++;
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 442, as _ZN24QSurfaceDataProxyPrivate7setItemEiiRK16QSurfaceDataItem
inline void QSurfaceDataProxyPrivate::setItem(int rowIndex, int columnIndex, const QSurfaceDataItem &item)
{
    Q_ASSERT(rowIndex >= 0 && rowIndex < m_dataArray->size());
    QSurfaceDataRow &row = *(*m_dataArray)[rowIndex];
    Q_ASSERT(columnIndex < row.size());
    row[columnIndex] = item;
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 450, as _ZN24QSurfaceDataProxyPrivate6addRowEP5QListI16QSurfaceDataItemE
inline int QSurfaceDataProxyPrivate::addRow(QSurfaceDataRow *row)
{
    Q_ASSERT(m_dataArray->isEmpty()
             || m_dataArray->at(0)->size() == row->size());
    int currentSize = m_dataArray->size();
    m_dataArray->append(row);
    return currentSize;
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 459, as _ZN24QSurfaceDataProxyPrivate7addRowsERK5QListIPS0_I16QSurfaceDataItemEE
inline int QSurfaceDataProxyPrivate::addRows(const QSurfaceDataArray &rows)
{
    int currentSize = m_dataArray->size();
    for (int i = 0; i < rows.size(); i++) {
        Q_ASSERT(m_dataArray->isEmpty()
                 || m_dataArray->at(0)->size() == rows.at(i)->size());
        m_dataArray->append(rows.at(i));
    }
    return currentSize;
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 470, as _ZN24QSurfaceDataProxyPrivate9insertRowEiP5QListI16QSurfaceDataItemE
inline void QSurfaceDataProxyPrivate::insertRow(int rowIndex, QSurfaceDataRow *row)
{
    Q_ASSERT(rowIndex >= 0 && rowIndex <= m_dataArray->size());
    Q_ASSERT(m_dataArray->isEmpty()
             || m_dataArray->at(0)->size() == row->size());
    m_dataArray->insert(rowIndex, row);
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 478, as _ZN24QSurfaceDataProxyPrivate10insertRowsEiRK5QListIPS0_I16QSurfaceDataItemEE
inline void QSurfaceDataProxyPrivate::insertRows(int rowIndex, const QSurfaceDataArray &rows)
{
    Q_ASSERT(rowIndex >= 0 && rowIndex <= m_dataArray->size());

    for (int i = 0; i < rows.size(); i++) {
        Q_ASSERT(m_dataArray->isEmpty()
                 || m_dataArray->at(0)->size() == rows.at(i)->size());
        m_dataArray->insert(rowIndex++, rows.at(i));
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 489, as _ZN24QSurfaceDataProxyPrivate10removeRowsEii
inline void QSurfaceDataProxyPrivate::removeRows(int rowIndex, int removeCount)
{
    Q_ASSERT(rowIndex >= 0);
    int maxRemoveCount = m_dataArray->size() - rowIndex;
    removeCount = qMin(removeCount, maxRemoveCount);
    for (int i = 0; i < removeCount; i++) {
        clearRow(rowIndex);
        m_dataArray->removeAt(rowIndex);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 505, as _ZNK24QSurfaceDataProxyPrivate11limitValuesER9QVector3DS1_P15QAbstract3DAxisS3_S3_
inline void QSurfaceDataProxyPrivate::limitValues(QVector3D &minValues, QVector3D &maxValues,
                                           QAbstract3DAxis *axisX, QAbstract3DAxis *axisY,
                                           QAbstract3DAxis *axisZ) const
{
    float min = 0.0f;
    float max = 0.0f;

    int rows = m_dataArray->size();
    int columns = 0;
    if (rows)
        columns = m_dataArray->at(0)->size();

    if (rows && columns) {
        min = m_dataArray->at(0)->at(0).y();
        max = m_dataArray->at(0)->at(0).y();
    }

    for (int i = 0; i < rows; i++) {
        QSurfaceDataRow *row = m_dataArray->at(i);
        if (row) {
            for (int j = 0; j < columns; j++) {
                float itemValue = m_dataArray->at(i)->at(j).y();
                if (qIsNaN(itemValue) || qIsInf(itemValue))
                    continue;
                if ((min > itemValue || (qIsNaN(min) || qIsInf(min)))
                        && isValidValue(itemValue, axisY)) {
                    min = itemValue;
                }
                if (max < itemValue  || (qIsNaN(max) || qIsInf(max)))
                    max = itemValue;
            }
        }
    }

    minValues.setY(min);
    maxValues.setY(max);

    if (columns) {
        // Have some defaults
        float xLow = m_dataArray->at(0)->at(0).x();
        float xHigh = m_dataArray->at(0)->last().x();
        float zLow = m_dataArray->at(0)->at(0).z();
        float zHigh = m_dataArray->last()->at(0).z();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                float zItemValue = m_dataArray->at(i)->at(j).z();
                if (qIsNaN(zItemValue) || qIsInf(zItemValue))
                    continue;
                else if (isValidValue(zItemValue, axisZ))
                    zLow = qMin(zLow,zItemValue);
            }
            if (!qIsNaN(zLow) && !qIsInf(zLow))
                break;
        }
        for (int i = rows - 1; i >= 0; i--) {
            for (int j = 0; j < columns; j++) {
                float zItemValue = m_dataArray->at(i)->at(j).z();
                if (qIsNaN(zItemValue) || qIsInf(zItemValue))
                    continue;
                else if (isValidValue(zItemValue, axisZ))
                {
                    if (!qIsNaN(zHigh) && !qIsInf(zHigh))
                        zHigh = qMax(zHigh, zItemValue);
                    else
                        zHigh = zItemValue;
                }
            }
            if (!qIsNaN(zHigh) && !qIsInf(zHigh))
                break;
        }
        for (int j = 0; j<columns; j++){
            for (int i = 0; i < rows; i++) {
                float xItemValue = m_dataArray->at(i)->at(j).x();
                if (qIsNaN(xItemValue) || qIsInf(xItemValue))
                    continue;
                else if (isValidValue(xItemValue, axisX))
                    xLow = qMin(xLow, xItemValue);
            }
            if (!qIsNaN(xLow) && !qIsInf(xLow))
                break;
        }
        for (int j = columns-1; j >= 0; j--){
            for (int i = 0; i < rows; i++) {
                float xItemValue = m_dataArray->at(i)->at(j).x();
                if (qIsNaN(xItemValue) || qIsInf(xItemValue))
                    continue;
                else if (isValidValue(xItemValue, axisX))
                {
                    if (!qIsNaN(xHigh) && !qIsInf(xHigh))
                        xHigh = qMax(xHigh, xItemValue);
                    else
                        xHigh = xItemValue;
                }
            }
            if (!qIsNaN(xHigh) && !qIsInf(xHigh))
                break;
        }
        minValues.setX(xLow);
        minValues.setZ(zLow);
        maxValues.setX(xHigh);
        maxValues.setZ(zHigh);
    } else {
        minValues.setX(axisX->d_ptr->allowZero() ? 0.0f : 1.0f);
        minValues.setZ(axisZ->d_ptr->allowZero() ? 0.0f : 1.0f);
        maxValues.setX(axisX->d_ptr->allowZero() ? 0.0f : 1.0f);
        maxValues.setZ(axisZ->d_ptr->allowZero() ? 0.0f : 1.0f);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 614, as _ZNK24QSurfaceDataProxyPrivate12isValidValueEfP15QAbstract3DAxis
inline bool QSurfaceDataProxyPrivate::isValidValue(float value, QAbstract3DAxis *axis) const
{
    return (value > 0.0f || (value == 0.0f && axis->d_ptr->allowZero())
            || (value < 0.0f && axis->d_ptr->allowNegatives()));
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 500, as _ZN24QSurfaceDataProxyPrivate4qptrEv
inline QSurfaceDataProxy *QSurfaceDataProxyPrivate::qptr()
{
    return static_cast<QSurfaceDataProxy *>(q_ptr);
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 620, as _ZN24QSurfaceDataProxyPrivate8clearRowEi
inline void QSurfaceDataProxyPrivate::clearRow(int rowIndex)
{
    if (m_dataArray->at(rowIndex)) {
        delete m_dataArray->at(rowIndex);
        (*m_dataArray)[rowIndex] = 0;
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 628, as _ZN24QSurfaceDataProxyPrivate10clearArrayEv
inline void QSurfaceDataProxyPrivate::clearArray()
{
    for (int i = 0; i < m_dataArray->size(); i++)
        clearRow(i);
    m_dataArray->clear();
    delete m_dataArray;
}
//  -----------------------------------------------------------------------

//  A QSurfaceDataProxyPrivate that Python can take functions over in. Every QSurfaceDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSurfaceDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurfaceDataProxyPrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurfaceDataProxyPrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyPrivateCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyPrivateCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyPrivateCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyPrivateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSurfaceDataProxyPrivate : public QSurfaceDataProxyPrivate {
public:
  using QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate;
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
      CuteQSurfaceDataProxyPrivateCall0 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall0>(taken[0]);
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
      CuteQSurfaceDataProxyPrivateCall1 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall1>(taken[1]);
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
      CuteQSurfaceDataProxyPrivateCall2 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall2>(taken[2]);
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
      CuteQSurfaceDataProxyPrivateCall3 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall3>(taken[3]);
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
      CuteQSurfaceDataProxyPrivateCall4 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall4>(taken[4]);
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
      CuteQSurfaceDataProxyPrivateCall5 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall5>(taken[5]);
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
      CuteQSurfaceDataProxyPrivateCall6 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall6>(taken[6]);
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
      CuteQSurfaceDataProxyPrivateCall7 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSurfaceDataProxyPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QSurfaceDataProxyPrivate10metaObjectEv(
    const QSurfaceDataProxyPrivate *self) {
  return self->metaObject();
}

//  void *QSurfaceDataProxyPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QSurfaceDataProxyPrivate11qt_metacastEPKc(
    QSurfaceDataProxyPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSurfaceDataProxyPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QSurfaceDataProxyPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QSurfaceDataProxyPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSurfaceDataProxyPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QSurfaceDataProxyPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSurfaceDataProxyPrivate::tr(s, c, n));
}

//  QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate(QSurfaceDataProxy *q)
extern "C" Q_DECL_EXPORT
QSurfaceDataProxyPrivate *ritual_ZN24QSurfaceDataProxyPrivateC1EP17QSurfaceDataProxy(
    QSurfaceDataProxy *q) {
  return new CuteQSurfaceDataProxyPrivate(q);
}

//  QSurfaceDataProxyPrivate::~QSurfaceDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivateD1Ev(
    QSurfaceDataProxyPrivate *self) {
  delete self;
}

//  void QSurfaceDataProxyPrivate::resetArray(QSurfaceDataArray *newArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate10resetArrayEP5QListIPS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxyPrivate *self,
    QSurfaceDataArray *newArray) {
  self->resetArray(newArray);
}

//  void QSurfaceDataProxyPrivate::setRow(int rowIndex, QSurfaceDataRow *row)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate6setRowEiP5QListI16QSurfaceDataItemE(
    QSurfaceDataProxyPrivate *self,
    int rowIndex,
    QSurfaceDataRow *row) {
  self->setRow(rowIndex, row);
}

//  void QSurfaceDataProxyPrivate::setRows(int rowIndex, const
//      QSurfaceDataArray &rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate7setRowsEiRK5QListIPS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxyPrivate *self,
    int rowIndex,
    const QSurfaceDataArray *rows) {
  self->setRows(rowIndex, *rows);
}

//  void QSurfaceDataProxyPrivate::setItem(int rowIndex, int columnIndex,
//      const QSurfaceDataItem &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate7setItemEiiRK16QSurfaceDataItem(
    QSurfaceDataProxyPrivate *self,
    int rowIndex,
    int columnIndex,
    const QSurfaceDataItem *item) {
  self->setItem(rowIndex, columnIndex, *item);
}

//  int QSurfaceDataProxyPrivate::addRow(QSurfaceDataRow *row)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QSurfaceDataProxyPrivate6addRowEP5QListI16QSurfaceDataItemE(
    QSurfaceDataProxyPrivate *self,
    QSurfaceDataRow *row) {
  return self->addRow(row);
}

//  int QSurfaceDataProxyPrivate::addRows(const QSurfaceDataArray &rows)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QSurfaceDataProxyPrivate7addRowsERK5QListIPS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxyPrivate *self,
    const QSurfaceDataArray *rows) {
  return self->addRows(*rows);
}

//  void QSurfaceDataProxyPrivate::insertRow(int rowIndex, QSurfaceDataRow
//      *row)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate9insertRowEiP5QListI16QSurfaceDataItemE(
    QSurfaceDataProxyPrivate *self,
    int rowIndex,
    QSurfaceDataRow *row) {
  self->insertRow(rowIndex, row);
}

//  void QSurfaceDataProxyPrivate::insertRows(int rowIndex, const
//      QSurfaceDataArray &rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate10insertRowsEiRK5QListIPS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxyPrivate *self,
    int rowIndex,
    const QSurfaceDataArray *rows) {
  self->insertRows(rowIndex, *rows);
}

//  void QSurfaceDataProxyPrivate::removeRows(int rowIndex, int removeCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate10removeRowsEii(
    QSurfaceDataProxyPrivate *self,
    int rowIndex,
    int removeCount) {
  self->removeRows(rowIndex, removeCount);
}

//  void QSurfaceDataProxyPrivate::limitValues(QVector3D &minValues,
//      QVector3D &maxValues, QAbstract3DAxis *axisX, QAbstract3DAxis *axisY,
//      QAbstract3DAxis *axisZ) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QSurfaceDataProxyPrivate11limitValuesER9QVector3DS1_P15QAbstract3DAxisS3_S3_(
    const QSurfaceDataProxyPrivate *self,
    QVector3D *minValues,
    QVector3D *maxValues,
    QAbstract3DAxis *axisX,
    QAbstract3DAxis *axisY,
    QAbstract3DAxis *axisZ) {
  self->limitValues(*minValues, *maxValues, axisX, axisY, axisZ);
}

//  bool QSurfaceDataProxyPrivate::isValidValue(float value, QAbstract3DAxis
//      *axis) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSurfaceDataProxyPrivate12isValidValueEfP15QAbstract3DAxis(
    const QSurfaceDataProxyPrivate *self,
    float value,
    QAbstract3DAxis *axis) {
  return self->isValidValue(value, axis);
}

//  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QSurfaceDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->setSeries(series);
}

//  QSurfaceDataProxy *QSurfaceDataProxyPrivate::qptr()
extern "C" Q_DECL_EXPORT
QSurfaceDataProxy *ritual_ZN24QSurfaceDataProxyPrivate4qptrEv(
    QSurfaceDataProxyPrivate *self) {
  return self->qptr();
}

//  void QSurfaceDataProxyPrivate::clearRow(int rowIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate8clearRowEi(
    QSurfaceDataProxyPrivate *self,
    int rowIndex) {
  self->clearRow(rowIndex);
}

//  void QSurfaceDataProxyPrivate::clearArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate10clearArrayEv(
    QSurfaceDataProxyPrivate *self) {
  self->clearArray();
}

//  a Python function taken by a CuteQSurfaceDataProxyPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSurfaceDataProxyPrivate(
    QSurfaceDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSurfaceDataProxyPrivate *>(self)->take(key, call);
}

//  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QSurfaceDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->QSurfaceDataProxyPrivate::setSeries(series);
}
