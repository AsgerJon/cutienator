//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include "qcombobox_p.h"
#include <qstylepainter.h>
#include <qpa/qplatformtheme.h>
#include <qpa/qplatformmenu.h>
#include <qpa/qplatformwindow.h>
#include <qpa/qplatformwindow_p.h>
#include <qlineedit.h>
#include <qapplication.h>
#include <qlistview.h>
#if QT_CONFIG(tableview)
#include <qtableview.h>
#endif
#include <qabstractitemdelegate.h>
#include <qmap.h>
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#include <qevent.h>
#include <qlayout.h>
#include <qscrollbar.h>
#if QT_CONFIG(treeview)
#include <qtreeview.h>
#endif
#include <qheaderview.h>
#include <qmath.h>
#include <qmetaobject.h>
#if QT_CONFIG(proxymodel)
#include <qabstractproxymodel.h>
#endif
#include <qstylehints.h>
#include <private/qguiapplication_p.h>
#include <private/qhighdpiscaling_p.h>
#include <private/qapplication_p.h>
#include <private/qabstractitemmodel_p.h>
#include <private/qabstractscrollarea_p.h>
#include <private/qlineedit_p.h>
#if QT_CONFIG(completer)
#include <private/qcompleter_p.h>
#endif
#include <qdebug.h>
#if QT_CONFIG(effects)
# include <private/qeffects_p.h>
#endif
#include <private/qstyle_p.h>
#if QT_CONFIG(accessibility)
#include "qaccessible.h"
#endif
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtGui/qpainter.h>
#include <QtCore/qpointer.h>
#include <array>
#include <chrono>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/widgets/qcombobox.cpp, line 235, as _ZNK18QComboMenuDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex
inline void QComboMenuDelegate::paint(QPainter *painter, const QStyleOptionViewItem &option,
                               const QModelIndex &index) const
{
    const QStyleOptionMenuItem opt = getStyleOption(option, index);
    painter->fillRect(option.rect, opt.palette.window());
    mCombo->style()->drawControl(QStyle::CE_MenuItem, &opt, painter, mCombo);
}

//  from src/widgets/widgets/qcombobox.cpp, line 243, as _ZNK18QComboMenuDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex
inline QSize QComboMenuDelegate::sizeHint(const QStyleOptionViewItem &option,
                                   const QModelIndex &index) const
{
    const QStyleOptionMenuItem opt = getStyleOption(option, index);
    return mCombo->style()->sizeFromContents(QStyle::CT_MenuItem, &opt,
                                             option.rect.size(), mCombo);
}

//  from src/widgets/widgets/qcombobox.cpp, line 331, as _ZN18QComboMenuDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex
inline bool QComboMenuDelegate::editorEvent(QEvent *event, QAbstractItemModel *model,
                                     const QStyleOptionViewItem &option, const QModelIndex &index)
{
    Q_ASSERT(event);
    Q_ASSERT(model);

    // make sure that the item is checkable
    Qt::ItemFlags flags = model->flags(index);
    if (!(flags & Qt::ItemIsUserCheckable) || !(option.state & QStyle::State_Enabled)
        || !(flags & Qt::ItemIsEnabled))
        return false;

    // make sure that we have a check state
    const QVariant checkState = index.data(Qt::CheckStateRole);
    if (!checkState.isValid())
        return false;

    // make sure that we have the right event type
    if ((event->type() == QEvent::MouseButtonRelease)
        || (event->type() == QEvent::MouseButtonDblClick)
        || (event->type() == QEvent::MouseButtonPress)) {
        QMouseEvent *me = static_cast<QMouseEvent*>(event);
        if (me->button() != Qt::LeftButton)
            return false;

        if ((event->type() == QEvent::MouseButtonPress)
            || (event->type() == QEvent::MouseButtonDblClick)) {
            pressedIndex = index.row();
            return false;
        }

        if (index.row() != pressedIndex)
            return false;
        pressedIndex = -1;

    } else if (event->type() == QEvent::KeyPress) {
        if (static_cast<QKeyEvent*>(event)->key() != Qt::Key_Space
         && static_cast<QKeyEvent*>(event)->key() != Qt::Key_Select)
            return false;
    } else {
        return false;
    }

    // we don't support user-tristate items in QComboBox (not implemented in any style)
    Qt::CheckState newState = (static_cast<Qt::CheckState>(checkState.toInt()) == Qt::Checked)
                            ? Qt::Unchecked : Qt::Checked;
    return model->setData(index, newState, Qt::CheckStateRole);
}
//  -----------------------------------------------------------------------

//  Only a class built on QComboMenuDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQComboMenuDelegate : QComboMenuDelegate {
  using QComboMenuDelegate::editorEvent;
};

//  A QComboMenuDelegate that Python can take functions over in. Every QComboMenuDelegate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQComboMenuDelegateCall0)(const void *, QPainter *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef const QSize * (*CuteQComboMenuDelegateCall1)(const void *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef bool (*CuteQComboMenuDelegateCall2)(const void *, QEvent *, QAbstractItemModel *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef void * (*CuteQComboMenuDelegateCall3)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef void (*CuteQComboMenuDelegateCall4)(const void *, QWidget *, const QModelIndex *, int *);
typedef void (*CuteQComboMenuDelegateCall5)(const void *, QWidget *, const QModelIndex *, int *);
typedef void (*CuteQComboMenuDelegateCall6)(const void *, QWidget *, QAbstractItemModel *, const QModelIndex *, int *);
typedef void (*CuteQComboMenuDelegateCall7)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef bool (*CuteQComboMenuDelegateCall8)(const void *, QHelpEvent *, QAbstractItemView *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef bool (*CuteQComboMenuDelegateCall9)(const void *, QEvent *, int *);
typedef bool (*CuteQComboMenuDelegateCall10)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQComboMenuDelegateCall11)(const void *, QTimerEvent *, int *);
typedef void (*CuteQComboMenuDelegateCall12)(const void *, QChildEvent *, int *);
typedef void (*CuteQComboMenuDelegateCall13)(const void *, QEvent *, int *);
typedef void (*CuteQComboMenuDelegateCall14)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQComboMenuDelegateCall15)(const void *, const QMetaMethod *, int *);
class CuteQComboMenuDelegate : public QComboMenuDelegate {
public:
  using QComboMenuDelegate::QComboMenuDelegate;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17QAbstractItemViewRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
    return false;
  }

  //  void QComboMenuDelegate::paint(QPainter *painter, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  void paint(
      QPainter *painter,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQComboMenuDelegateCall0 call = reinterpret_cast<CuteQComboMenuDelegateCall0>(taken[0]);
      call(this, painter, &option, &index, &handled);
      if (handled) return;
    }
    QComboMenuDelegate::paint(painter, option, index);
  }

  //  QSize QComboMenuDelegate::sizeHint(const QStyleOptionViewItem
  //      &option, const QModelIndex &index) const
  QSize sizeHint(
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQComboMenuDelegateCall1 call = reinterpret_cast<CuteQComboMenuDelegateCall1>(taken[1]);
      const QSize * given = call(this, &option, &index, &handled);
      if (handled && given) return *given;
    }
    return QComboMenuDelegate::sizeHint(option, index);
  }

  //  bool QComboMenuDelegate::editorEvent(QEvent *event,
  //      QAbstractItemModel *model, const QStyleOptionViewItem &option,
  //      const QModelIndex &index)
  bool editorEvent(
      QEvent *event,
      QAbstractItemModel *model,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) override {
    if (taken[2]) {
      int handled = 0;
      CuteQComboMenuDelegateCall2 call = reinterpret_cast<CuteQComboMenuDelegateCall2>(taken[2]);
      bool given = call(this, event, model, &option, &index, &handled);
      if (handled) return given;
    }
    return QComboMenuDelegate::editorEvent(event, model, option, index);
  }

  //  QWidget *QAbstractItemDelegate::createEditor(QWidget *parent, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  QWidget *createEditor(
      QWidget *parent,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQComboMenuDelegateCall3 call = reinterpret_cast<CuteQComboMenuDelegateCall3>(taken[3]);
      void * given = call(this, parent, &option, &index, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QAbstractItemDelegate::createEditor(parent, option, index);
  }

  //  void QAbstractItemDelegate::destroyEditor(QWidget *editor, const
  //      QModelIndex &index) const
  void destroyEditor(
      QWidget *editor,
      const QModelIndex &index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQComboMenuDelegateCall4 call = reinterpret_cast<CuteQComboMenuDelegateCall4>(taken[4]);
      call(this, editor, &index, &handled);
      if (handled) return;
    }
    QAbstractItemDelegate::destroyEditor(editor, index);
  }

  //  void QAbstractItemDelegate::setEditorData(QWidget *editor, const
  //      QModelIndex &index) const
  void setEditorData(
      QWidget *editor,
      const QModelIndex &index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQComboMenuDelegateCall5 call = reinterpret_cast<CuteQComboMenuDelegateCall5>(taken[5]);
      call(this, editor, &index, &handled);
      if (handled) return;
    }
    QAbstractItemDelegate::setEditorData(editor, index);
  }

  //  void QAbstractItemDelegate::setModelData(QWidget *editor,
  //      QAbstractItemModel *model, const QModelIndex &index) const
  void setModelData(
      QWidget *editor,
      QAbstractItemModel *model,
      const QModelIndex &index) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQComboMenuDelegateCall6 call = reinterpret_cast<CuteQComboMenuDelegateCall6>(taken[6]);
      call(this, editor, model, &index, &handled);
      if (handled) return;
    }
    QAbstractItemDelegate::setModelData(editor, model, index);
  }

  //  void QAbstractItemDelegate::updateEditorGeometry(QWidget *editor,
  //      const QStyleOptionViewItem &option, const QModelIndex &index)
  //      const
  void updateEditorGeometry(
      QWidget *editor,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQComboMenuDelegateCall7 call = reinterpret_cast<CuteQComboMenuDelegateCall7>(taken[7]);
      call(this, editor, &option, &index, &handled);
      if (handled) return;
    }
    QAbstractItemDelegate::updateEditorGeometry(editor, option, index);
  }

  //  bool QAbstractItemDelegate::helpEvent(QHelpEvent *event,
  //      QAbstractItemView *view, const QStyleOptionViewItem &option,
  //      const QModelIndex &index)
  bool helpEvent(
      QHelpEvent *event,
      QAbstractItemView *view,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) override {
    if (taken[8]) {
      int handled = 0;
      CuteQComboMenuDelegateCall8 call = reinterpret_cast<CuteQComboMenuDelegateCall8>(taken[8]);
      bool given = call(this, event, view, &option, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemDelegate::helpEvent(event, view, option, index);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQComboMenuDelegateCall9 call = reinterpret_cast<CuteQComboMenuDelegateCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQComboMenuDelegateCall10 call = reinterpret_cast<CuteQComboMenuDelegateCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQComboMenuDelegateCall11 call = reinterpret_cast<CuteQComboMenuDelegateCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQComboMenuDelegateCall12 call = reinterpret_cast<CuteQComboMenuDelegateCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQComboMenuDelegateCall13 call = reinterpret_cast<CuteQComboMenuDelegateCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQComboMenuDelegateCall14 call = reinterpret_cast<CuteQComboMenuDelegateCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQComboMenuDelegateCall15 call = reinterpret_cast<CuteQComboMenuDelegateCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QComboMenuDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QComboMenuDelegate10metaObjectEv(
    const QComboMenuDelegate *self) {
  return self->metaObject();
}

//  void QComboMenuDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QComboMenuDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QComboMenuDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->paint(painter, *option, *index);
}

//  QSize QComboMenuDelegate::sizeHint(const QStyleOptionViewItem &option,
//      const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QComboMenuDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const QComboMenuDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(self->sizeHint(*option, *index));
}

//  bool QComboMenuDelegate::editorEvent(QEvent *event, QAbstractItemModel
//      *model, const QStyleOptionViewItem &option, const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QComboMenuDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex(
    QComboMenuDelegate *self,
    QEvent *event,
    QAbstractItemModel *model,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->editorEvent(event, model, *option, *index);
}

//  a Python function taken by a CuteQComboMenuDelegate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QComboMenuDelegate(
    QComboMenuDelegate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQComboMenuDelegate *>(self)->take(key, call);
}

//  bool QComboMenuDelegate::editorEvent(QEvent *event, QAbstractItemModel
//      *model, const QStyleOptionViewItem &option, const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QComboMenuDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex(
    QComboMenuDelegate *self,
    QEvent *event,
    QAbstractItemModel *model,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return static_cast<OwnQComboMenuDelegate *>(self)->OwnQComboMenuDelegate::editorEvent(
      event,
      model,
      *option,
      *index);
}
