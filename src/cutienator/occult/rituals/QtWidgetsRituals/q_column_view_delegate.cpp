//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcolumnview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcolumnview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qglobal.h>
#include <QtWidgets/qcolumnview.h>
#if QT_CONFIG(columnview)
#include <QtWidgets/private/qcolumnview_p.h>
#include <QtWidgets/private/qcolumnviewgrip_p.h>
#include <QtWidgets/qlistview.h>
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtWidgets/qscrollbar.h>
#include <QtGui/qpainter.h>
#include <QtCore/qdebug.h>
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

//  from src/widgets/itemviews/qcolumnview.cpp, line 1165, as _ZNK19QColumnViewDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex
#if QT_CONFIG(columnview)
inline void QColumnViewDelegate::paint(QPainter *painter,
                          const QStyleOptionViewItem &option,
                          const QModelIndex &index) const
{
    bool reverse = (option.direction == Qt::RightToLeft);
    int width = ((option.rect.height() * 2) / 3);
    // Modify the options to give us room to add an arrow
    QStyleOptionViewItem opt = option;
    if (reverse)
        opt.rect.adjust(width,0,0,0);
    else
        opt.rect.adjust(0,0,-width,0);

    if (!(index.model()->flags(index) & Qt::ItemIsEnabled)) {
        opt.showDecorationSelected = true;
        opt.state |= QStyle::State_Selected;
    }

    QStyledItemDelegate::paint(painter, opt, index);

    if (reverse)
        opt.rect = QRect(option.rect.x(), option.rect.y(), width, option.rect.height());
    else
        opt.rect = QRect(option.rect.x() + option.rect.width() - width, option.rect.y(),
                         width, option.rect.height());

    // Draw >
    if (index.model()->hasChildren(index)) {
        const QWidget *view = opt.widget;
        QStyle *style = view ? view->style() : QApplication::style();
        style->drawPrimitive(QStyle::PE_IndicatorColumnViewArrow, &opt, painter, view);
    }
}
#endif  // QT_CONFIG(columnview)
//  -----------------------------------------------------------------------

//  A QColumnViewDelegate that Python can take functions over in. Every QColumnViewDelegate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(columnview)
typedef void (*CuteQColumnViewDelegateCall0)(const void *, QPainter *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(columnview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QSize * (*CuteQColumnViewDelegateCall1)(const void *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQColumnViewDelegateCall2)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewDelegateCall3)(const void *, QWidget *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewDelegateCall4)(const void *, QWidget *, QAbstractItemModel *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewDelegateCall5)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef QString * (*CuteQColumnViewDelegateCall6)(const void *, const QVariant *, const QLocale *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewDelegateCall7)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQColumnViewDelegateCall8)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQColumnViewDelegateCall9)(const void *, QEvent *, QAbstractItemModel *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewDelegateCall10)(const void *, QWidget *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQColumnViewDelegateCall11)(const void *, QHelpEvent *, QAbstractItemView *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQColumnViewDelegateCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColumnViewDelegateCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColumnViewDelegateCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColumnViewDelegateCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColumnViewDelegateCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColumnViewDelegateCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQColumnViewDelegate : public QColumnViewDelegate {
public:
  using QColumnViewDelegate::QColumnViewDelegate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
#if QT_CONFIG(columnview)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(columnview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK19QStyledItemDelegate11displayTextERK8QVariantRK7QLocale")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK19QStyledItemDelegate15initStyleOptionEP20QStyleOptionViewItemRK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17QAbstractItemViewRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemviews)
#if QT_CONFIG(columnview)
  //  void QColumnViewDelegate::paint(QPainter *painter, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  void paint(
      QPainter *painter,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQColumnViewDelegateCall0 call = reinterpret_cast<CuteQColumnViewDelegateCall0>(taken[0]);
      call(this, painter, &option, &index, &handled);
      if (handled) return;
    }
    QColumnViewDelegate::paint(painter, option, index);
  }
#endif  // QT_CONFIG(columnview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QSize QStyledItemDelegate::sizeHint(const QStyleOptionViewItem
  //      &option, const QModelIndex &index) const
  QSize sizeHint(
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQColumnViewDelegateCall1 call = reinterpret_cast<CuteQColumnViewDelegateCall1>(taken[1]);
      const QSize * given = call(this, &option, &index, &handled);
      if (handled && given) return *given;
    }
    return QStyledItemDelegate::sizeHint(option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QWidget *QStyledItemDelegate::createEditor(QWidget *parent, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  QWidget *createEditor(
      QWidget *parent,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQColumnViewDelegateCall2 call = reinterpret_cast<CuteQColumnViewDelegateCall2>(taken[2]);
      void * given = call(this, parent, &option, &index, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QStyledItemDelegate::createEditor(parent, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QStyledItemDelegate::setEditorData(QWidget *editor, const
  //      QModelIndex &index) const
  void setEditorData(
      QWidget *editor,
      const QModelIndex &index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQColumnViewDelegateCall3 call = reinterpret_cast<CuteQColumnViewDelegateCall3>(taken[3]);
      call(this, editor, &index, &handled);
      if (handled) return;
    }
    QStyledItemDelegate::setEditorData(editor, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QStyledItemDelegate::setModelData(QWidget *editor,
  //      QAbstractItemModel *model, const QModelIndex &index) const
  void setModelData(
      QWidget *editor,
      QAbstractItemModel *model,
      const QModelIndex &index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQColumnViewDelegateCall4 call = reinterpret_cast<CuteQColumnViewDelegateCall4>(taken[4]);
      call(this, editor, model, &index, &handled);
      if (handled) return;
    }
    QStyledItemDelegate::setModelData(editor, model, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QStyledItemDelegate::updateEditorGeometry(QWidget *editor, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  void updateEditorGeometry(
      QWidget *editor,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQColumnViewDelegateCall5 call = reinterpret_cast<CuteQColumnViewDelegateCall5>(taken[5]);
      call(this, editor, &option, &index, &handled);
      if (handled) return;
    }
    QStyledItemDelegate::updateEditorGeometry(editor, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QString QStyledItemDelegate::displayText(const QVariant &value, const
  //      QLocale &locale) const
  QString displayText(
      const QVariant &value,
      const QLocale &locale) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQColumnViewDelegateCall6 call = reinterpret_cast<CuteQColumnViewDelegateCall6>(taken[6]);
      QString * given = call(this, &value, &locale, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QStyledItemDelegate::displayText(value, locale);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QStyledItemDelegate::initStyleOption(QStyleOptionViewItem
  //      *option, const QModelIndex &index) const
  void initStyleOption(
      QStyleOptionViewItem *option,
      const QModelIndex &index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQColumnViewDelegateCall7 call = reinterpret_cast<CuteQColumnViewDelegateCall7>(taken[7]);
      call(this, option, &index, &handled);
      if (handled) return;
    }
    QStyledItemDelegate::initStyleOption(option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
  //  bool QStyledItemDelegate::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQColumnViewDelegateCall8 call = reinterpret_cast<CuteQColumnViewDelegateCall8>(taken[8]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QStyledItemDelegate::eventFilter(object, event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(itemviews)
  //  bool QStyledItemDelegate::editorEvent(QEvent *event,
  //      QAbstractItemModel *model, const QStyleOptionViewItem &option,
  //      const QModelIndex &index)
  bool editorEvent(
      QEvent *event,
      QAbstractItemModel *model,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) override {
    if (taken[9]) {
      int handled = 0;
      CuteQColumnViewDelegateCall9 call = reinterpret_cast<CuteQColumnViewDelegateCall9>(taken[9]);
      bool given = call(this, event, model, &option, &index, &handled);
      if (handled) return given;
    }
    return QStyledItemDelegate::editorEvent(event, model, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemDelegate::destroyEditor(QWidget *editor, const
  //      QModelIndex &index) const
  void destroyEditor(
      QWidget *editor,
      const QModelIndex &index) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQColumnViewDelegateCall10 call = reinterpret_cast<CuteQColumnViewDelegateCall10>(taken[10]);
      call(this, editor, &index, &handled);
      if (handled) return;
    }
    QAbstractItemDelegate::destroyEditor(editor, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemDelegate::helpEvent(QHelpEvent *event,
  //      QAbstractItemView *view, const QStyleOptionViewItem &option,
  //      const QModelIndex &index)
  bool helpEvent(
      QHelpEvent *event,
      QAbstractItemView *view,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) override {
    if (taken[11]) {
      int handled = 0;
      CuteQColumnViewDelegateCall11 call = reinterpret_cast<CuteQColumnViewDelegateCall11>(taken[11]);
      bool given = call(this, event, view, &option, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemDelegate::helpEvent(event, view, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQColumnViewDelegateCall12 call = reinterpret_cast<CuteQColumnViewDelegateCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQColumnViewDelegateCall13 call = reinterpret_cast<CuteQColumnViewDelegateCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQColumnViewDelegateCall14 call = reinterpret_cast<CuteQColumnViewDelegateCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQColumnViewDelegateCall15 call = reinterpret_cast<CuteQColumnViewDelegateCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQColumnViewDelegateCall16 call = reinterpret_cast<CuteQColumnViewDelegateCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQColumnViewDelegateCall17 call = reinterpret_cast<CuteQColumnViewDelegateCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

#if QT_CONFIG(columnview)
//  QColumnViewDelegate::QColumnViewDelegate(QObject *parent)
extern "C" Q_DECL_EXPORT
QColumnViewDelegate *ritual_ZN19QColumnViewDelegateC1EP7QObject(
    QObject *parent) {
  return new CuteQColumnViewDelegate(parent);
}
#endif  // QT_CONFIG(columnview)

//  QColumnViewDelegate::~QColumnViewDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QColumnViewDelegateD1Ev(QColumnViewDelegate *self) {
  delete self;
}

//  void QColumnViewDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QColumnViewDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QColumnViewDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->paint(painter, *option, *index);
}

//  a Python function taken by a CuteQColumnViewDelegate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QColumnViewDelegate(
    QColumnViewDelegate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQColumnViewDelegate *>(self)->take(key, call);
}

#if QT_CONFIG(columnview)
//  void QColumnViewDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QColumnViewDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QColumnViewDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->QColumnViewDelegate::paint(painter, *option, *index);
}
#endif  // QT_CONFIG(columnview)

#endif  // QT_CONFIG(columnview)
#endif  // QT_CONFIG(columnview)
