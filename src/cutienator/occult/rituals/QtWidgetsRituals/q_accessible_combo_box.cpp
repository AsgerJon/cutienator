//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/complexwidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/complexwidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/complexwidgets_p.h>
#include <QtGui/qaccessible.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qevent.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qheaderview.h>
#endif
#if QT_CONFIG(tabbar)
#include <QtWidgets/qtabbar.h>
#include <QtWidgets/private/qtabbar_p.h>
#endif
#if QT_CONFIG(combobox)
#include <QtWidgets/qcombobox.h>
#endif
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#if QT_CONFIG(whatsthis)
#include <QtWidgets/qwhatsthis.h>
#endif
#include <QtWidgets/QAbstractScrollArea>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/QScrollArea>
#endif
#if QT_CONFIG(scrollbar)
#include <QtWidgets/QScrollBar>
#endif
#include <QtCore/QDebug>
#if QT_CONFIG(accessibility)
#include <QtGui/private/qaccessiblehelper_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/accessible/complexwidgets.cpp, line 341, as _ZN19QAccessibleComboBoxC1EP7QWidget
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
inline QAccessibleComboBox::QAccessibleComboBox(QWidget *w)
: QAccessibleWidgetV2(w, QAccessible::ComboBox)
{
    Q_ASSERT(comboBox());
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 369, as _ZNK19QAccessibleComboBox10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
inline int QAccessibleComboBox::childCount() const
{
    // list and text edit
    if (QComboBox *cBox = comboBox())
        return (cBox->isEditable()) ? 2 : 1;
    return 0;
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 377, as _ZNK19QAccessibleComboBox7childAtEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
inline QAccessibleInterface *QAccessibleComboBox::childAt(int x, int y) const
{
    if (QComboBox *cBox = comboBox()) {
        if (cBox->isEditable() && cBox->lineEdit()->rect().contains(x, y))
            return child(1);
    }
    return nullptr;
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 386, as _ZNK19QAccessibleComboBox12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
inline int QAccessibleComboBox::indexOfChild(const QAccessibleInterface *child) const
{
    if (QComboBox *cBox = comboBox()) {
        if (cBox->view() == child->object())
            return 0;
        if (cBox->isEditable() && cBox->lineEdit() == child->object())
            return 1;
    }
    return -1;
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 355, as _ZNK19QAccessibleComboBox5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
inline QAccessibleInterface *QAccessibleComboBox::child(int index) const
{
    if (QComboBox *cBox = comboBox()) {
        if (index == 0) {
            QAbstractItemView *view = cBox->view();
            //QWidget *parent = view ? view->parentWidget() : 0;
            return QAccessible::queryAccessibleInterface(view);
        } else if (index == 1 && cBox->isEditable()) {
            return QAccessible::queryAccessibleInterface(cBox->lineEdit());
        }
    }
    return nullptr;
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 397, as _ZNK19QAccessibleComboBox10focusChildEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
inline QAccessibleInterface *QAccessibleComboBox::focusChild() const
{
    // The editable combobox is the focus proxy of its lineedit, so the
    // lineedit itself never gets focus. But it is the accessible focus
    // child of an editable combobox.
    if (QComboBox *cBox = comboBox()) {
        if (cBox->isEditable())
            return child(1);
    }
    return nullptr;
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 410, as _ZNK19QAccessibleComboBox4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
#if defined(Q_OS_LINUX)
inline QString QAccessibleComboBox::text(QAccessible::Text t) const
{
    QString str;
    if (QComboBox *cBox = comboBox()) {
        switch (t) {
        case QAccessible::Name:
#ifndef Q_OS_UNIX // on Linux we use relations for this, name is text (fall through to Value)
        str = QAccessibleWidgetV2::text(t);
        break;
#endif
        case QAccessible::Value:
            if (cBox->isEditable())
                str = cBox->lineEdit()->text();
            else
                str = cBox->currentText();
            break;
#ifndef QT_NO_SHORTCUT
        case QAccessible::Accelerator:
            str = QKeySequence(Qt::Key_Down).toString(QKeySequence::NativeText);
            break;
#endif
        default:
            break;
        }
        if (str.isEmpty())
            str = QAccessibleWidgetV2::text(t);
    }
    return str;
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 440, as _ZNK19QAccessibleComboBox5stateEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
inline QAccessible::State QAccessibleComboBox::state() const
{
    QAccessible::State s = QAccessibleWidgetV2::state();

    if (QComboBox *cBox = comboBox()) {
        s.expandable = true;
        s.expanded = isValid() && cBox->view() && cBox->view()->isVisible();
        s.editable = cBox->isEditable();
    }
    return s;
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 452, as _ZNK19QAccessibleComboBox11actionNamesEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
inline QStringList QAccessibleComboBox::actionNames() const
{
    return QStringList() << showMenuAction() << pressAction();
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 457, as _ZNK19QAccessibleComboBox26localizedActionDescriptionERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
inline QString QAccessibleComboBox::localizedActionDescription(const QString &actionName) const
{
    if (actionName == showMenuAction() || actionName == pressAction())
        return QComboBox::tr("Open the combo box selection popup");
    return QString();
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 464, as _ZN19QAccessibleComboBox8doActionERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
#if defined(Q_OS_LINUX)
inline void QAccessibleComboBox::doAction(const QString &actionName)
{
    if (QComboBox *cBox = comboBox()) {
        if (actionName == showMenuAction() || actionName == pressAction()) {
            if (cBox->view()->isVisible()) {
#if defined(Q_OS_ANDROID)
                const auto list = child(0)->tableInterface();
                if (list && list->selectedRowCount() > 0) {
                    cBox->setCurrentIndex(list->selectedRows().at(0));
                }
                cBox->setFocus();
#endif
                cBox->hidePopup();
            } else {
                cBox->showPopup();
#if defined(Q_OS_ANDROID)
                const auto list = child(0)->tableInterface();
                if (list && list->selectedRowCount() > 0) {
                    auto selectedCells = list->selectedCells();
                    QAccessibleEvent ev(selectedCells.at(0),QAccessible::Focus);
                    QAccessible::updateAccessibility(&ev);
                }
#endif
            }
        }
    }
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 492, as _ZNK19QAccessibleComboBox20keyBindingsForActionERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
inline QStringList QAccessibleComboBox::keyBindingsForAction(const QString &/*actionName*/) const
{
    return QStringList();
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 350, as _ZNK19QAccessibleComboBox8comboBoxEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
inline QComboBox *QAccessibleComboBox::comboBox() const
{
    return qobject_cast<QComboBox *>(object());
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleComboBox that Python can take functions over in. Every QAccessibleComboBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
typedef int (*CuteQAccessibleComboBoxCall0)(const void *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
typedef void * (*CuteQAccessibleComboBoxCall1)(const void *, int, int, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
typedef int (*CuteQAccessibleComboBoxCall2)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
typedef void * (*CuteQAccessibleComboBoxCall3)(const void *, int, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
typedef void * (*CuteQAccessibleComboBoxCall4)(const void *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
typedef QString * (*CuteQAccessibleComboBoxCall5)(const void *, int, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
typedef const QAccessible::State * (*CuteQAccessibleComboBoxCall6)(const void *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
typedef QString * (*CuteQAccessibleComboBoxCall7)(const void *, const QString *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
typedef void (*CuteQAccessibleComboBoxCall8)(const void *, const QString *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleComboBoxCall9)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleComboBoxCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleComboBoxCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleComboBoxCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleComboBoxCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleComboBoxCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleComboBoxCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleComboBoxCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleComboBoxCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleComboBoxCall18)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleComboBoxCall19)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleComboBox : public QAccessibleComboBox {
public:
  using QAccessibleComboBox::QAccessibleComboBox;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
  //  int QAccessibleComboBox::childCount() const
  int childCount() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall0 call = reinterpret_cast<CuteQAccessibleComboBoxCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleComboBox::childCount();
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
  //  QAccessibleInterface *QAccessibleComboBox::childAt(int x, int y)
  //      const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall1 call = reinterpret_cast<CuteQAccessibleComboBoxCall1>(taken[1]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleComboBox::childAt(x, y);
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
  //  int QAccessibleComboBox::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall2 call = reinterpret_cast<CuteQAccessibleComboBoxCall2>(taken[2]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleComboBox::indexOfChild(child);
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
  //  QAccessibleInterface *QAccessibleComboBox::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall3 call = reinterpret_cast<CuteQAccessibleComboBoxCall3>(taken[3]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleComboBox::child(index);
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
  //  QAccessibleInterface *QAccessibleComboBox::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall4 call = reinterpret_cast<CuteQAccessibleComboBoxCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleComboBox::focusChild();
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
  //  QString QAccessibleComboBox::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall5 call = reinterpret_cast<CuteQAccessibleComboBoxCall5>(taken[5]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleComboBox::text(t);
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
  //  QAccessible::State QAccessibleComboBox::state() const
  QAccessible::State state() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall6 call = reinterpret_cast<CuteQAccessibleComboBoxCall6>(taken[6]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleComboBox::state();
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
  //  QString QAccessibleComboBox::localizedActionDescription(const QString
  //      &actionName) const
  QString localizedActionDescription(
      const QString &actionName) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall7 call = reinterpret_cast<CuteQAccessibleComboBoxCall7>(taken[7]);
      QString * given = call(this, &actionName, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleComboBox::localizedActionDescription(actionName);
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
  //  void QAccessibleComboBox::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall8 call = reinterpret_cast<CuteQAccessibleComboBoxCall8>(taken[8]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleComboBox::doAction(actionName);
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall9 call = reinterpret_cast<CuteQAccessibleComboBoxCall9>(taken[9]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall10 call = reinterpret_cast<CuteQAccessibleComboBoxCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall11 call = reinterpret_cast<CuteQAccessibleComboBoxCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall12 call = reinterpret_cast<CuteQAccessibleComboBoxCall12>(taken[12]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall13 call = reinterpret_cast<CuteQAccessibleComboBoxCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall14 call = reinterpret_cast<CuteQAccessibleComboBoxCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall15 call = reinterpret_cast<CuteQAccessibleComboBoxCall15>(taken[15]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall16 call = reinterpret_cast<CuteQAccessibleComboBoxCall16>(taken[16]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall17 call = reinterpret_cast<CuteQAccessibleComboBoxCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleObject::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall18 call = reinterpret_cast<CuteQAccessibleComboBoxCall18>(taken[18]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleComboBoxCall19 call = reinterpret_cast<CuteQAccessibleComboBoxCall19>(taken[19]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionName(name);
  }
#endif  // QT_CONFIG(accessibility)
};

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
#if defined(Q_OS_LINUX)
//  QAccessibleComboBox::QAccessibleComboBox(QWidget *w)
extern "C" Q_DECL_EXPORT
QAccessibleComboBox *ritual_ZN19QAccessibleComboBoxC1EP7QWidget(QWidget *w) {
  return new CuteQAccessibleComboBox(w);
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  int QAccessibleComboBox::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAccessibleComboBox10childCountEv(
    const QAccessibleComboBox *self) {
  return self->childCount();
}

//  QAccessibleInterface *QAccessibleComboBox::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK19QAccessibleComboBox7childAtEii(
    const QAccessibleComboBox *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

//  int QAccessibleComboBox::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAccessibleComboBox12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleComboBox *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  QAccessibleInterface *QAccessibleComboBox::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK19QAccessibleComboBox5childEi(
    const QAccessibleComboBox *self,
    int index) {
  return self->child(index);
}

//  QAccessibleInterface *QAccessibleComboBox::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK19QAccessibleComboBox10focusChildEv(
    const QAccessibleComboBox *self) {
  return self->focusChild();
}

//  QString QAccessibleComboBox::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAccessibleComboBox4textEN11QAccessible4TextE(
    const QAccessibleComboBox *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessible::State QAccessibleComboBox::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK19QAccessibleComboBox5stateEv(
    const QAccessibleComboBox *self) {
  return new QAccessible::State(self->state());
}

//  QStringList QAccessibleComboBox::actionNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QAccessibleComboBox11actionNamesEv(
    const QAccessibleComboBox *self) {
  return new QList<QString>(self->actionNames());
}

//  QString QAccessibleComboBox::localizedActionDescription(const QString
//      &actionName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAccessibleComboBox26localizedActionDescriptionERK7QString(
    const QAccessibleComboBox *self,
    const QString *actionName) {
  return new QString(self->localizedActionDescription(*actionName));
}

//  void QAccessibleComboBox::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleComboBox8doActionERK7QString(
    QAccessibleComboBox *self,
    const QString *actionName) {
  self->doAction(*actionName);
}

//  QStringList QAccessibleComboBox::keyBindingsForAction(const QString
//      &actionName) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QAccessibleComboBox20keyBindingsForActionERK7QString(
    const QAccessibleComboBox *self,
    const QString *actionName) {
  return new QList<QString>(self->keyBindingsForAction(*actionName));
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
//  QComboBox *QAccessibleComboBox::comboBox() const
extern "C" Q_DECL_EXPORT
QComboBox *ritual_ZNK19QAccessibleComboBox8comboBoxEv(
    const QAccessibleComboBox *self) {
  return self->comboBox();
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleComboBox, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleComboBox(
    QAccessibleComboBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleComboBox *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
//  int QAccessibleComboBox::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAccessibleComboBox10childCountEv(
    const QAccessibleComboBox *self) {
  return self->QAccessibleComboBox::childCount();
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
//  QAccessibleInterface *QAccessibleComboBox::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK19QAccessibleComboBox7childAtEii(
    const QAccessibleComboBox *self,
    int x,
    int y) {
  return self->QAccessibleComboBox::childAt(x, y);
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
//  int QAccessibleComboBox::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAccessibleComboBox12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleComboBox *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleComboBox::indexOfChild(child);
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
//  QAccessibleInterface *QAccessibleComboBox::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK19QAccessibleComboBox5childEi(
    const QAccessibleComboBox *self,
    int index) {
  return self->QAccessibleComboBox::child(index);
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
//  QAccessibleInterface *QAccessibleComboBox::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK19QAccessibleComboBox10focusChildEv(
    const QAccessibleComboBox *self) {
  return self->QAccessibleComboBox::focusChild();
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
#if defined(Q_OS_LINUX)
//  QString QAccessibleComboBox::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QAccessibleComboBox4textEN11QAccessible4TextE(
    const QAccessibleComboBox *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleComboBox::text(t));
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
//  QAccessible::State QAccessibleComboBox::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK19QAccessibleComboBox5stateEv(
    const QAccessibleComboBox *self) {
  return new QAccessible::State(self->QAccessibleComboBox::state());
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
//  QString QAccessibleComboBox::localizedActionDescription(const QString
//      &actionName) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QAccessibleComboBox26localizedActionDescriptionERK7QString(
    const QAccessibleComboBox *self,
    const QString *actionName) {
  return new QString(
      self->QAccessibleComboBox::localizedActionDescription(
          *actionName));
}
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(combobox)
#if defined(Q_OS_LINUX)
//  void QAccessibleComboBox::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleComboBox8doActionERK7QString(
    QAccessibleComboBox *self,
    const QString *actionName) {
  self->QAccessibleComboBox::doAction(*actionName);
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
