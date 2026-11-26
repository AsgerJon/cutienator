//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qcombobox_p.h>
#include <QtWidgets/qstylepainter.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/qpa/qplatformmenu.h>
#include <QtGui/qpa/qplatformwindow.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qlistview.h>
#if QT_CONFIG(tableview)
#include <QtWidgets/qtableview.h>
#endif
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtCore/qmap.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtGui/qevent.h>
#include <QtWidgets/qlayout.h>
#include <QtWidgets/qscrollbar.h>
#if QT_CONFIG(treeview)
#include <QtWidgets/qtreeview.h>
#endif
#include <QtWidgets/qheaderview.h>
#include <QtCore/qmath.h>
#include <QtCore/qmetaobject.h>
#if QT_CONFIG(proxymodel)
#include <QtCore/qabstractproxymodel.h>
#endif
#include <QtGui/qstylehints.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtWidgets/private/qabstractscrollarea_p.h>
#include <QtWidgets/private/qlineedit_p.h>
#if QT_CONFIG(completer)
#include <QtWidgets/private/qcompleter_p.h>
#endif
#include <QtCore/qdebug.h>
#if QT_CONFIG(effects)
# include <QtWidgets/private/qeffects_p.h>
#endif
#include <QtWidgets/private/qstyle_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtGui/qpainter.h>
#include <QtCore/qpointer.h>
#include <array>
#include <chrono>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qcombobox.cpp, line 407, as _ZNK17QComboBoxDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex
inline void QComboBoxDelegate::paint(QPainter *painter, const QStyleOptionViewItem &option,
                              const QModelIndex &index) const
{
    if (isSeparator(index)) {
        QRect rect = option.rect;
        if (const QAbstractItemView *view = qobject_cast<const QAbstractItemView*>(option.widget))
            rect.setWidth(view->viewport()->width());
        QStyleOption opt;
        opt.rect = rect;
        mCombo->style()->drawPrimitive(QStyle::PE_IndicatorToolBarSeparator,
                                       &opt, painter, mCombo);
    } else {
        QStyledItemDelegate::paint(painter, option, index);
    }
}

//  from src/widgets/widgets/qcombobox.cpp, line 423, as _ZNK17QComboBoxDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex
inline QSize QComboBoxDelegate::sizeHint(const QStyleOptionViewItem &option,
                                  const QModelIndex &index) const
{
    if (isSeparator(index)) {
        const int pm = mCombo->style()->pixelMetric(QStyle::PM_DefaultFrameWidth, nullptr, mCombo);
        return QSize(pm, pm);
    }
    return QStyledItemDelegate::sizeHint(option, index);
}

//  from src/widgets/widgets/qcombobox.cpp, line 392, as _ZN17QComboBoxDelegate11isSeparatorERK11QModelIndex
inline bool QComboBoxDelegate::isSeparator(const QModelIndex &index)
{
    return index.data(Qt::AccessibleDescriptionRole).toString() == "separator"_L1;
}

//  from src/widgets/widgets/qcombobox.cpp, line 397, as _ZN17QComboBoxDelegate12setSeparatorEP18QAbstractItemModelRK11QModelIndex
inline void QComboBoxDelegate::setSeparator(QAbstractItemModel *model, const QModelIndex &index)
{
    // don't use u""_s; model (QtCore) may outlive QtWidgets DLL, alloc dynamically:
    static const QString sepString = "separator"_L1;
    model->setData(index, sepString, Qt::AccessibleDescriptionRole);
    if (QStandardItemModel *m = qobject_cast<QStandardItemModel*>(model))
        if (QStandardItem *item = m->itemFromIndex(index))
            item->setFlags(item->flags() & ~(Qt::ItemIsSelectable|Qt::ItemIsEnabled));
}
//  -----------------------------------------------------------------------

//  Only a class built on QComboBoxDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQComboBoxDelegate : QComboBoxDelegate {
  using QComboBoxDelegate::paint;
  using QComboBoxDelegate::sizeHint;
};

//  A QComboBoxDelegate that Python can take functions over in. Every QComboBoxDelegate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxDelegateCall0)(const void *, QPainter *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(combobox)
typedef const QSize * (*CuteQComboBoxDelegateCall1)(const void *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQComboBoxDelegateCall2)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxDelegateCall3)(const void *, QWidget *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxDelegateCall4)(const void *, QWidget *, QAbstractItemModel *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxDelegateCall5)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef QString * (*CuteQComboBoxDelegateCall6)(const void *, const QVariant *, const QLocale *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxDelegateCall7)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQComboBoxDelegateCall8)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQComboBoxDelegateCall9)(const void *, QEvent *, QAbstractItemModel *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxDelegateCall10)(const void *, QWidget *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQComboBoxDelegateCall11)(const void *, QHelpEvent *, QAbstractItemView *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQComboBoxDelegateCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxDelegateCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxDelegateCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxDelegateCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxDelegateCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxDelegateCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQComboBoxDelegate : public QComboBoxDelegate {
public:
  using QComboBoxDelegate::QComboBoxDelegate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
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
#if QT_CONFIG(combobox)
  //  void QComboBoxDelegate::paint(QPainter *painter, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  void paint(
      QPainter *painter,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQComboBoxDelegateCall0 call = reinterpret_cast<CuteQComboBoxDelegateCall0>(taken[0]);
      call(this, painter, &option, &index, &handled);
      if (handled) return;
    }
    QComboBoxDelegate::paint(painter, option, index);
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(combobox)
  //  QSize QComboBoxDelegate::sizeHint(const QStyleOptionViewItem &option,
  //      const QModelIndex &index) const
  QSize sizeHint(
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQComboBoxDelegateCall1 call = reinterpret_cast<CuteQComboBoxDelegateCall1>(taken[1]);
      const QSize * given = call(this, &option, &index, &handled);
      if (handled && given) return *given;
    }
    return QComboBoxDelegate::sizeHint(option, index);
  }
#endif  // QT_CONFIG(combobox)
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
      CuteQComboBoxDelegateCall2 call = reinterpret_cast<CuteQComboBoxDelegateCall2>(taken[2]);
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
      CuteQComboBoxDelegateCall3 call = reinterpret_cast<CuteQComboBoxDelegateCall3>(taken[3]);
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
      CuteQComboBoxDelegateCall4 call = reinterpret_cast<CuteQComboBoxDelegateCall4>(taken[4]);
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
      CuteQComboBoxDelegateCall5 call = reinterpret_cast<CuteQComboBoxDelegateCall5>(taken[5]);
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
      CuteQComboBoxDelegateCall6 call = reinterpret_cast<CuteQComboBoxDelegateCall6>(taken[6]);
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
      CuteQComboBoxDelegateCall7 call = reinterpret_cast<CuteQComboBoxDelegateCall7>(taken[7]);
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
      CuteQComboBoxDelegateCall8 call = reinterpret_cast<CuteQComboBoxDelegateCall8>(taken[8]);
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
      CuteQComboBoxDelegateCall9 call = reinterpret_cast<CuteQComboBoxDelegateCall9>(taken[9]);
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
      CuteQComboBoxDelegateCall10 call = reinterpret_cast<CuteQComboBoxDelegateCall10>(taken[10]);
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
      CuteQComboBoxDelegateCall11 call = reinterpret_cast<CuteQComboBoxDelegateCall11>(taken[11]);
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
      CuteQComboBoxDelegateCall12 call = reinterpret_cast<CuteQComboBoxDelegateCall12>(taken[12]);
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
      CuteQComboBoxDelegateCall13 call = reinterpret_cast<CuteQComboBoxDelegateCall13>(taken[13]);
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
      CuteQComboBoxDelegateCall14 call = reinterpret_cast<CuteQComboBoxDelegateCall14>(taken[14]);
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
      CuteQComboBoxDelegateCall15 call = reinterpret_cast<CuteQComboBoxDelegateCall15>(taken[15]);
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
      CuteQComboBoxDelegateCall16 call = reinterpret_cast<CuteQComboBoxDelegateCall16>(taken[16]);
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
      CuteQComboBoxDelegateCall17 call = reinterpret_cast<CuteQComboBoxDelegateCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QComboBoxDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QComboBoxDelegate10metaObjectEv(
    const QComboBoxDelegate *self) {
  return self->metaObject();
}

//  void *QComboBoxDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QComboBoxDelegate11qt_metacastEPKc(
    QComboBoxDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QComboBoxDelegate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QComboBoxDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    QComboBoxDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QComboBoxDelegate::~QComboBoxDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QComboBoxDelegateD1Ev(QComboBoxDelegate *self) {
  delete self;
}

//  bool QComboBoxDelegate::isSeparator(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QComboBoxDelegate11isSeparatorERK11QModelIndex(
    const QModelIndex *index) {
  return QComboBoxDelegate::isSeparator(*index);
}

//  void QComboBoxDelegate::setSeparator(QAbstractItemModel *model, const
//      QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QComboBoxDelegate12setSeparatorEP18QAbstractItemModelRK11QModelIndex(
    QAbstractItemModel *model,
    const QModelIndex *index) {
  QComboBoxDelegate::setSeparator(model, *index);
}

//  void QComboBoxDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QComboBoxDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QComboBoxDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->paint(painter, *option, *index);
}

//  QSize QComboBoxDelegate::sizeHint(const QStyleOptionViewItem &option,
//      const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QComboBoxDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const QComboBoxDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(self->sizeHint(*option, *index));
}

//  a Python function taken by a CuteQComboBoxDelegate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QComboBoxDelegate(
    QComboBoxDelegate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQComboBoxDelegate *>(self)->take(key, call);
}

//  void QComboBoxDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK17QComboBoxDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QComboBoxDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  static_cast<const OwnQComboBoxDelegate *>(self)->OwnQComboBoxDelegate::paint(
      painter,
      *option,
      *index);
}

//  QSize QComboBoxDelegate::sizeHint(const QStyleOptionViewItem &option,
//      const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK17QComboBoxDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const QComboBoxDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(
      static_cast<const OwnQComboBoxDelegate *>(self)->OwnQComboBoxDelegate::sizeHint(
          *option,
          *index));
}

#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(combobox)
