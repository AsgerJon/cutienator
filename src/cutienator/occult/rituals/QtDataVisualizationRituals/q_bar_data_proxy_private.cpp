//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/qbardataproxy_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qbardataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/qbardataitem.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QPair>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/qbardataproxy_p.h>
#include <QtDataVisualization/private/qbar3dseries_p.h>
#include <QtDataVisualization/private/qabstractdataproxy_p.h>
#include <QtDataVisualization/private/qabstract3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 757, as _ZN20QBarDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    QAbstractDataProxyPrivate::setSeries(series);
    QBar3DSeries *barSeries = static_cast<QBar3DSeries *>(series);
    emit qptr()->seriesChanged(barSeries);
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstractdataproxy.cpp, line 97, as _ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    q_ptr->setParent(series);
    m_series = series;
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 540, as _ZN20QBarDataProxyPrivate10resetArrayEP5QListIPS0_I12QBarDataItemEEPKS0_I7QStringES9_
inline void QBarDataProxyPrivate::resetArray(QBarDataArray *newArray, const QStringList *rowLabels,
                                      const QStringList *columnLabels)
{
    if (rowLabels)
        qptr()->setRowLabels(*rowLabels);
    if (columnLabels)
        qptr()->setColumnLabels(*columnLabels);

    if (!newArray)
        newArray = new QBarDataArray;

    if (newArray != m_dataArray) {
        clearArray();
        m_dataArray = newArray;
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 557, as _ZN20QBarDataProxyPrivate6setRowEiP5QListI12QBarDataItemEPK7QString
inline void QBarDataProxyPrivate::setRow(int rowIndex, QBarDataRow *row, const QString *label)
{
    Q_ASSERT(rowIndex >= 0 && rowIndex < m_dataArray->size());

    if (label)
        fixRowLabels(rowIndex, 1, QStringList(*label), false);
    if (row != m_dataArray->at(rowIndex)) {
        clearRow(rowIndex);
        (*m_dataArray)[rowIndex] = row;
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 569, as _ZN20QBarDataProxyPrivate7setRowsEiRK5QListIPS0_I12QBarDataItemEEPKS0_I7QStringE
inline void QBarDataProxyPrivate::setRows(int rowIndex, const QBarDataArray &rows,
                                   const QStringList *labels)
{
    QBarDataArray &dataArray = *m_dataArray;
    Q_ASSERT(rowIndex >= 0 && (rowIndex + rows.size()) <= dataArray.size());
    if (labels)
        fixRowLabels(rowIndex, rows.size(), *labels, false);
    for (int i = 0; i < rows.size(); i++) {
        if (rows.at(i) != dataArray.at(rowIndex)) {
            clearRow(rowIndex);
            dataArray[rowIndex] = rows.at(i);
        }
        rowIndex++;
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 585, as _ZN20QBarDataProxyPrivate7setItemEiiRK12QBarDataItem
inline void QBarDataProxyPrivate::setItem(int rowIndex, int columnIndex, const QBarDataItem &item)
{
    Q_ASSERT(rowIndex >= 0 && rowIndex < m_dataArray->size());
    QBarDataRow &row = *(*m_dataArray)[rowIndex];
    Q_ASSERT(columnIndex < row.size());
    row[columnIndex] = item;
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 593, as _ZN20QBarDataProxyPrivate6addRowEP5QListI12QBarDataItemEPK7QString
inline int QBarDataProxyPrivate::addRow(QBarDataRow *row, const QString *label)
{
    int currentSize = m_dataArray->size();
    if (label)
        fixRowLabels(currentSize, 1, QStringList(*label), false);
    m_dataArray->append(row);
    return currentSize;
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 602, as _ZN20QBarDataProxyPrivate7addRowsERK5QListIPS0_I12QBarDataItemEEPKS0_I7QStringE
inline int QBarDataProxyPrivate::addRows(const QBarDataArray &rows, const QStringList *labels)
{
    int currentSize = m_dataArray->size();
    if (labels)
        fixRowLabels(currentSize, rows.size(), *labels, false);
    for (int i = 0; i < rows.size(); i++)
        m_dataArray->append(rows.at(i));
    return currentSize;
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 612, as _ZN20QBarDataProxyPrivate9insertRowEiP5QListI12QBarDataItemEPK7QString
inline void QBarDataProxyPrivate::insertRow(int rowIndex, QBarDataRow *row, const QString *label)
{
    Q_ASSERT(rowIndex >= 0 && rowIndex <= m_dataArray->size());
    if (label)
        fixRowLabels(rowIndex, 1, QStringList(*label), true);
    m_dataArray->insert(rowIndex, row);
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 620, as _ZN20QBarDataProxyPrivate10insertRowsEiRK5QListIPS0_I12QBarDataItemEEPKS0_I7QStringE
inline void QBarDataProxyPrivate::insertRows(int rowIndex, const QBarDataArray &rows,
                                      const QStringList *labels)
{
    Q_ASSERT(rowIndex >= 0 && rowIndex <= m_dataArray->size());
    if (labels)
        fixRowLabels(rowIndex, rows.size(), *labels, true);
    for (int i = 0; i < rows.size(); i++)
        m_dataArray->insert(rowIndex++, rows.at(i));
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 630, as _ZN20QBarDataProxyPrivate10removeRowsEiib
inline void QBarDataProxyPrivate::removeRows(int rowIndex, int removeCount, bool removeLabels)
{
    Q_ASSERT(rowIndex >= 0);
    int maxRemoveCount = m_dataArray->size() - rowIndex;
    removeCount = qMin(removeCount, maxRemoveCount);
    bool labelsChanged = false;
    for (int i = 0; i < removeCount; i++) {
        clearRow(rowIndex);
        m_dataArray->removeAt(rowIndex);
        if (removeLabels && m_rowLabels.size() > rowIndex) {
            m_rowLabels.removeAt(rowIndex);
            labelsChanged = true;
        }
    }
    if (labelsChanged)
        emit qptr()->rowLabelsChanged();
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 735, as _ZNK20QBarDataProxyPrivate11limitValuesEiiii
inline QPair<GLfloat, GLfloat> QBarDataProxyPrivate::limitValues(int startRow, int endRow,
                                                          int startColumn, int endColumn) const
{
    QPair<GLfloat, GLfloat> limits = qMakePair(0.0f, 0.0f);
    endRow = qMin(endRow, m_dataArray->size() - 1);
    for (int i = startRow; i <= endRow; i++) {
        QBarDataRow *row = m_dataArray->at(i);
        if (row) {
            int lastColumn = qMin(endColumn, row->size() - 1);
            for (int j = startColumn; j <= lastColumn; j++) {
                const QBarDataItem &item = row->at(j);
                float itemValue = item.value();
                if (limits.second < itemValue)
                    limits.second = itemValue;
                if (limits.first > itemValue)
                    limits.first = itemValue;
            }
        }
    }
    return limits;
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 648, as _ZN20QBarDataProxyPrivate4qptrEv
inline QBarDataProxy *QBarDataProxyPrivate::qptr()
{
    return static_cast<QBarDataProxy *>(q_ptr);
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 653, as _ZN20QBarDataProxyPrivate8clearRowEi
inline void QBarDataProxyPrivate::clearRow(int rowIndex)
{
    if (m_dataArray->at(rowIndex)) {
        delete m_dataArray->at(rowIndex);
        (*m_dataArray)[rowIndex] = 0;
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 661, as _ZN20QBarDataProxyPrivate10clearArrayEv
inline void QBarDataProxyPrivate::clearArray()
{
    for (int i = 0; i < m_dataArray->size(); i++)
        clearRow(i);
    m_dataArray->clear();
    delete m_dataArray;
}

//  from ../qtdatavis3d/src/datavisualization/data/qbardataproxy.cpp, line 673, as _ZN20QBarDataProxyPrivate12fixRowLabelsEiiRK5QListI7QStringEb
inline void QBarDataProxyPrivate::fixRowLabels(int startIndex, int count, const QStringList &newLabels,
                                        bool isInsert)
{
    bool changed = false;
    int currentSize = m_rowLabels.size();

    int newSize = newLabels.size();
    if (startIndex >= currentSize) {
        // Adding labels past old label array, create empty strings to fill intervening space
        if (newSize) {
            for (int i = currentSize; i < startIndex; i++)
                m_rowLabels << QString();
            // Doesn't matter if insert, append, or just change when there were no existing
            // strings, just append new strings.
            m_rowLabels << newLabels;
            changed = true;
        }
    } else {
        if (isInsert) {
            int insertIndex = startIndex;
            if (count)
                changed = true;
            for (int i = 0; i < count; i++) {
                if (i < newSize)
                    m_rowLabels.insert(insertIndex++, newLabels.at(i));
                else
                    m_rowLabels.insert(insertIndex++, QString());
            }
        } else {
            // Either append or change, replace labels up to array end and then add new ones
            int lastChangeIndex = count + startIndex;
            int newIndex = 0;
            for (int i = startIndex; i < lastChangeIndex; i++) {
                if (i >= currentSize) {
                    // Label past the current size, so just append the new label
                    if (newSize < newIndex) {
                        changed = true;
                        m_rowLabels << newLabels.at(newIndex);
                    } else {
                        break; // No point appending empty strings, so just exit
                    }
                } else if (newSize > newIndex) {
                    // Replace existing label
                    if (m_rowLabels.at(i) != newLabels.at(newIndex)) {
                        changed = true;
                        m_rowLabels[i] = newLabels.at(newIndex);
                    }
                } else {
                    // No more new labels, so clear existing label
                    if (!m_rowLabels.at(i).isEmpty()) {
                        changed = true;
                        m_rowLabels[i] = QString();
                    }
                }
                newIndex++;
            }
        }
    }
    if (changed)
        emit qptr()->rowLabelsChanged();
}
//  -----------------------------------------------------------------------

//  A QBarDataProxyPrivate that Python can take functions over in. Every QBarDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQBarDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarDataProxyPrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarDataProxyPrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarDataProxyPrivateCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarDataProxyPrivateCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarDataProxyPrivateCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarDataProxyPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarDataProxyPrivateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBarDataProxyPrivate : public QBarDataProxyPrivate {
public:
  using QBarDataProxyPrivate::QBarDataProxyPrivate;
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

  //  void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBarDataProxyPrivateCall0 call = reinterpret_cast<CuteQBarDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QBarDataProxyPrivate::setSeries(series);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQBarDataProxyPrivateCall1 call = reinterpret_cast<CuteQBarDataProxyPrivateCall1>(taken[1]);
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
      CuteQBarDataProxyPrivateCall2 call = reinterpret_cast<CuteQBarDataProxyPrivateCall2>(taken[2]);
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
      CuteQBarDataProxyPrivateCall3 call = reinterpret_cast<CuteQBarDataProxyPrivateCall3>(taken[3]);
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
      CuteQBarDataProxyPrivateCall4 call = reinterpret_cast<CuteQBarDataProxyPrivateCall4>(taken[4]);
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
      CuteQBarDataProxyPrivateCall5 call = reinterpret_cast<CuteQBarDataProxyPrivateCall5>(taken[5]);
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
      CuteQBarDataProxyPrivateCall6 call = reinterpret_cast<CuteQBarDataProxyPrivateCall6>(taken[6]);
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
      CuteQBarDataProxyPrivateCall7 call = reinterpret_cast<CuteQBarDataProxyPrivateCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBarDataProxyPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QBarDataProxyPrivate10metaObjectEv(
    const QBarDataProxyPrivate *self) {
  return self->metaObject();
}

//  void *QBarDataProxyPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QBarDataProxyPrivate11qt_metacastEPKc(
    QBarDataProxyPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBarDataProxyPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QBarDataProxyPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QBarDataProxyPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QBarDataProxyPrivate::~QBarDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivateD1Ev(QBarDataProxyPrivate *self) {
  delete self;
}

//  void QBarDataProxyPrivate::resetArray(QBarDataArray *newArray, const
//      QStringList *rowLabels, const QStringList *columnLabels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate10resetArrayEP5QListIPS0_I12QBarDataItemEEPKS0_I7QStringES9_(
    QBarDataProxyPrivate *self,
    QBarDataArray *newArray,
    const QStringList *rowLabels,
    const QStringList *columnLabels) {
  self->resetArray(newArray, rowLabels, columnLabels);
}

//  void QBarDataProxyPrivate::setRow(int rowIndex, QBarDataRow *row, const
//      QString *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate6setRowEiP5QListI12QBarDataItemEPK7QString(
    QBarDataProxyPrivate *self,
    int rowIndex,
    QBarDataRow *row,
    const QString *label) {
  self->setRow(rowIndex, row, label);
}

//  void QBarDataProxyPrivate::setRows(int rowIndex, const QBarDataArray
//      &rows, const QStringList *labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate7setRowsEiRK5QListIPS0_I12QBarDataItemEEPKS0_I7QStringE(
    QBarDataProxyPrivate *self,
    int rowIndex,
    const QBarDataArray *rows,
    const QStringList *labels) {
  self->setRows(rowIndex, *rows, labels);
}

//  void QBarDataProxyPrivate::setItem(int rowIndex, int columnIndex, const
//      QBarDataItem &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate7setItemEiiRK12QBarDataItem(
    QBarDataProxyPrivate *self,
    int rowIndex,
    int columnIndex,
    const QBarDataItem *item) {
  self->setItem(rowIndex, columnIndex, *item);
}

//  int QBarDataProxyPrivate::addRow(QBarDataRow *row, const QString *label)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QBarDataProxyPrivate6addRowEP5QListI12QBarDataItemEPK7QString(
    QBarDataProxyPrivate *self,
    QBarDataRow *row,
    const QString *label) {
  return self->addRow(row, label);
}

//  int QBarDataProxyPrivate::addRows(const QBarDataArray &rows, const
//      QStringList *labels)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QBarDataProxyPrivate7addRowsERK5QListIPS0_I12QBarDataItemEEPKS0_I7QStringE(
    QBarDataProxyPrivate *self,
    const QBarDataArray *rows,
    const QStringList *labels) {
  return self->addRows(*rows, labels);
}

//  void QBarDataProxyPrivate::insertRow(int rowIndex, QBarDataRow *row,
//      const QString *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate9insertRowEiP5QListI12QBarDataItemEPK7QString(
    QBarDataProxyPrivate *self,
    int rowIndex,
    QBarDataRow *row,
    const QString *label) {
  self->insertRow(rowIndex, row, label);
}

//  void QBarDataProxyPrivate::insertRows(int rowIndex, const QBarDataArray
//      &rows, const QStringList *labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate10insertRowsEiRK5QListIPS0_I12QBarDataItemEEPKS0_I7QStringE(
    QBarDataProxyPrivate *self,
    int rowIndex,
    const QBarDataArray *rows,
    const QStringList *labels) {
  self->insertRows(rowIndex, *rows, labels);
}

//  void QBarDataProxyPrivate::removeRows(int rowIndex, int removeCount, bool
//      removeLabels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate10removeRowsEiib(
    QBarDataProxyPrivate *self,
    int rowIndex,
    int removeCount,
    bool removeLabels) {
  self->removeRows(rowIndex, removeCount, removeLabels);
}

//  QPair<GLfloat, GLfloat> QBarDataProxyPrivate::limitValues(int startRow,
//      int startColumn, int rowCount, int columnCount) const
extern "C" Q_DECL_EXPORT
QPair<GLfloat, GLfloat> *ritual_ZNK20QBarDataProxyPrivate11limitValuesEiiii(
    const QBarDataProxyPrivate *self,
    int startRow,
    int startColumn,
    int rowCount,
    int columnCount) {
  return new QPair<GLfloat, GLfloat>(
      self->limitValues(
          startRow,
          startColumn,
          rowCount,
          columnCount));
}

//  void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QBarDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->setSeries(series);
}

//  QBarDataProxy *QBarDataProxyPrivate::qptr()
extern "C" Q_DECL_EXPORT
QBarDataProxy *ritual_ZN20QBarDataProxyPrivate4qptrEv(
    QBarDataProxyPrivate *self) {
  return self->qptr();
}

//  void QBarDataProxyPrivate::clearRow(int rowIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate8clearRowEi(
    QBarDataProxyPrivate *self,
    int rowIndex) {
  self->clearRow(rowIndex);
}

//  void QBarDataProxyPrivate::clearArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate10clearArrayEv(
    QBarDataProxyPrivate *self) {
  self->clearArray();
}

//  void QBarDataProxyPrivate::fixRowLabels(int startIndex, int count, const
//      QStringList &newLabels, bool isInsert)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate12fixRowLabelsEiiRK5QListI7QStringEb(
    QBarDataProxyPrivate *self,
    int startIndex,
    int count,
    const QList<QString> *newLabels,
    bool isInsert) {
  self->fixRowLabels(startIndex, count, *newLabels, isInsert);
}

//  a Python function taken by a CuteQBarDataProxyPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarDataProxyPrivate(
    QBarDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBarDataProxyPrivate *>(self)->take(key, call);
}

//  void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QBarDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QBarDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->QBarDataProxyPrivate::setSeries(series);
}

//  a QPair<GLfloat, GLfloat> a ritual of QBarDataProxyPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QBarDataProxyPrivate__QPair_GLfloat_GLfloat(
    QPair<GLfloat, GLfloat> *self) {
  delete self;
}
