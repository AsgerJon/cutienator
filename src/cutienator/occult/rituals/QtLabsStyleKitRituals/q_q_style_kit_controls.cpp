//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrols_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qobject.h>
#include <QtCore/qlist.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrol.cpp, line 67, as _ZN17QQStyleKitControlC1EP7QObject
inline QQStyleKitControl::QQStyleKitControl(QObject *parent)
    : QQStyleKitControlState(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 676, as _ZN18QQStyleKitControls21set_applicationWindowEP17QQStyleKitControl
inline void QQStyleKitControls::set_applicationWindow(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::ApplicationWindow, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 675, as _ZN18QQStyleKitControls18set_abstractButtonEP17QQStyleKitControl
inline void QQStyleKitControls::set_abstractButton(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::AbstractButton, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 677, as _ZN18QQStyleKitControls11set_controlEP17QQStyleKitControl
inline void QQStyleKitControls::set_control(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::Control, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 678, as _ZN18QQStyleKitControls17set_busyIndicatorEP17QQStyleKitControl
inline void QQStyleKitControls::set_busyIndicator(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::BusyIndicator, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 679, as _ZN18QQStyleKitControls10set_buttonEP17QQStyleKitControl
inline void QQStyleKitControls::set_button(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::Button, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 681, as _ZN18QQStyleKitControls12set_checkBoxEP17QQStyleKitControl
inline void QQStyleKitControls::set_checkBox(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::CheckBox, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 682, as _ZN18QQStyleKitControls17set_checkDelegateEP17QQStyleKitControl
inline void QQStyleKitControls::set_checkDelegate(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::CheckDelegate, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 683, as _ZN18QQStyleKitControls12set_comboBoxEP17QQStyleKitControl
inline void QQStyleKitControls::set_comboBox(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::ComboBox, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 684, as _ZN18QQStyleKitControls15set_delayButtonEP17QQStyleKitControl
inline void QQStyleKitControls::set_delayButton(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::DelayButton, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 685, as _ZN18QQStyleKitControls8set_dialEP17QQStyleKitControl
inline void QQStyleKitControls::set_dial(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::Dial, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 686, as _ZN18QQStyleKitControls10set_dialogEP17QQStyleKitControl
inline void QQStyleKitControls::set_dialog(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::Dialog, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 687, as _ZN18QQStyleKitControls19set_dialogButtonBoxEP17QQStyleKitControl
inline void QQStyleKitControls::set_dialogButtonBox(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::DialogButtonBox, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 680, as _ZN18QQStyleKitControls14set_flatButtonEP17QQStyleKitControl
inline void QQStyleKitControls::set_flatButton(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::FlatButton, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 688, as _ZN18QQStyleKitControls15set_progressBarEP17QQStyleKitControl
inline void QQStyleKitControls::set_progressBar(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::ProgressBar, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 689, as _ZN18QQStyleKitControls13set_scrollBarEP17QQStyleKitControl
inline void QQStyleKitControls::set_scrollBar(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::ScrollBar, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 690, as _ZN18QQStyleKitControls19set_scrollIndicatorEP17QQStyleKitControl
inline void QQStyleKitControls::set_scrollIndicator(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::ScrollIndicator, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 691, as _ZN18QQStyleKitControls14set_scrollViewEP17QQStyleKitControl
inline void QQStyleKitControls::set_scrollView(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::ScrollView, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 692, as _ZN18QQStyleKitControls15set_searchFieldEP17QQStyleKitControl
inline void QQStyleKitControls::set_searchField(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::SearchField, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 693, as _ZN18QQStyleKitControls10set_sliderEP17QQStyleKitControl
inline void QQStyleKitControls::set_slider(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::Slider, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 694, as _ZN18QQStyleKitControls11set_spinBoxEP17QQStyleKitControl
inline void QQStyleKitControls::set_spinBox(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::SpinBox, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 698, as _ZN18QQStyleKitControls10set_tabBarEP17QQStyleKitControl
inline void QQStyleKitControls::set_tabBar(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::TabBar, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 699, as _ZN18QQStyleKitControls13set_tabButtonEP17QQStyleKitControl
inline void QQStyleKitControls::set_tabButton(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::TabButton, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 700, as _ZN18QQStyleKitControls13set_textFieldEP17QQStyleKitControl
inline void QQStyleKitControls::set_textField(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::TextField, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 701, as _ZN18QQStyleKitControls13set_textInputEP17QQStyleKitControl
inline void QQStyleKitControls::set_textInput(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::TextInput, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 702, as _ZN18QQStyleKitControls11set_toolBarEP17QQStyleKitControl
inline void QQStyleKitControls::set_toolBar(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::ToolBar, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 703, as _ZN18QQStyleKitControls14set_toolButtonEP17QQStyleKitControl
inline void QQStyleKitControls::set_toolButton(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::ToolButton, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 704, as _ZN18QQStyleKitControls17set_toolSeparatorEP17QQStyleKitControl
inline void QQStyleKitControls::set_toolSeparator(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::ToolSeparator, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 695, as _ZN18QQStyleKitControls17set_swipeDelegateEP17QQStyleKitControl
inline void QQStyleKitControls::set_swipeDelegate(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::SwipeDelegate, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 696, as _ZN18QQStyleKitControls17set_switchControlEP17QQStyleKitControl
inline void QQStyleKitControls::set_switchControl(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::SwitchControl, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 697, as _ZN18QQStyleKitControls18set_switchDelegateEP17QQStyleKitControl
inline void QQStyleKitControls::set_switchDelegate(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::SwitchDelegate, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 705, as _ZN18QQStyleKitControls15set_radioButtonEP17QQStyleKitControl
inline void QQStyleKitControls::set_radioButton(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::RadioButton, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 706, as _ZN18QQStyleKitControls17set_radioDelegateEP17QQStyleKitControl
inline void QQStyleKitControls::set_radioDelegate(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::RadioDelegate, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 707, as _ZN18QQStyleKitControls15set_roundButtonEP17QQStyleKitControl
inline void QQStyleKitControls::set_roundButton(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::RoundButton, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 708, as _ZN18QQStyleKitControls16set_itemDelegateEP17QQStyleKitControl
inline void QQStyleKitControls::set_itemDelegate(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::ItemDelegate, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 709, as _ZN18QQStyleKitControls9set_popupEP17QQStyleKitControl
inline void QQStyleKitControls::set_popup(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::Popup, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 710, as _ZN18QQStyleKitControls8set_paneEP17QQStyleKitControl
inline void QQStyleKitControls::set_pane(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::Pane, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 711, as _ZN18QQStyleKitControls8set_pageEP17QQStyleKitControl
inline void QQStyleKitControls::set_page(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::Page, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 712, as _ZN18QQStyleKitControls17set_pageIndicatorEP17QQStyleKitControl
inline void QQStyleKitControls::set_pageIndicator(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::PageIndicator, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 713, as _ZN18QQStyleKitControls9set_frameEP17QQStyleKitControl
inline void QQStyleKitControls::set_frame(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::Frame, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 714, as _ZN18QQStyleKitControls9set_labelEP17QQStyleKitControl
inline void QQStyleKitControls::set_label(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::Label, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 715, as _ZN18QQStyleKitControls12set_groupBoxEP17QQStyleKitControl
inline void QQStyleKitControls::set_groupBox(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::GroupBox, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 716, as _ZN18QQStyleKitControls12set_textAreaEP17QQStyleKitControl
inline void QQStyleKitControls::set_textArea(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::TextArea, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 717, as _ZN18QQStyleKitControls8set_menuEP17QQStyleKitControl
inline void QQStyleKitControls::set_menu(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::Menu, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 718, as _ZN18QQStyleKitControls11set_menuBarEP17QQStyleKitControl
inline void QQStyleKitControls::set_menuBar(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::MenuBar, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 719, as _ZN18QQStyleKitControls15set_menuBarItemEP17QQStyleKitControl
inline void QQStyleKitControls::set_menuBarItem(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::MenuBarItem, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 720, as _ZN18QQStyleKitControls12set_menuItemEP17QQStyleKitControl
inline void QQStyleKitControls::set_menuItem(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::MenuItem, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 721, as _ZN18QQStyleKitControls17set_menuSeparatorEP17QQStyleKitControl
inline void QQStyleKitControls::set_menuSeparator(QQStyleKitControl *control) { m_controls.insert(QQStyleKitReader::ControlType::MenuSeparator, control); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 725, as _ZN18QQStyleKitControls17componentCompleteEv
inline void QQStyleKitControls::componentComplete()
{
    for (auto *obj : children()) {
        if (auto *customControl = qobject_cast<QQStyleKitCustomControl *>(obj)) {
            const QQStyleKitExtendableControlType type = customControl->controlType();
            const QQStyleKitExtendableControlType reserved
                = QQStyleKitExtendableControlType(QQStyleKitReader::ControlType::Unspecified);
            if (type >= reserved)
                qmlWarning(this) << "CustomControls must use a controlType less than " << reserved;
            if (m_controls.contains(type))
                qmlWarning(this) << "CustomControl registered more than once: " << type;
            m_controls.insert(type, customControl);
        }
    }
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 654, as _ZNK18QQStyleKitControls15getControlStyleEj
inline QQStyleKitControl* QQStyleKitControls::getControlStyle(QQStyleKitExtendableControlType controlType) const
{
    return m_controls.value(controlType, nullptr);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 609, as _ZN18QQStyleKitControls4dataEv
inline QQmlListProperty<QObject> QQStyleKitControls::data()
{
    return QQmlListProperty<QObject>(this, &m_data);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 614, as _ZNK18QQStyleKitControls8childrenEv
inline const QList<QObject *> QQStyleKitControls::children() const
{
    return m_data;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQStyleKitControls may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQStyleKitControls : QQStyleKitControls {
  using QQStyleKitControls::classBegin;
};

//  const QMetaObject *QQStyleKitControls::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQStyleKitControls10metaObjectEv(
    const QQStyleKitControls *self) {
  return self->metaObject();
}

//  void *QQStyleKitControls::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQStyleKitControls11qt_metacastEPKc(
    QQStyleKitControls *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitControls::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQStyleKitControls11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitControls *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQStyleKitControls::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls24qt_qmlMarker_uncreatableEv(
    QQStyleKitControls *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQStyleKitControls::set_applicationWindow(QQStyleKitControl
//      *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls21set_applicationWindowEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_applicationWindow(control);
}

//  void QQStyleKitControls::set_abstractButton(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls18set_abstractButtonEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_abstractButton(control);
}

//  void QQStyleKitControls::set_control(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls11set_controlEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_control(control);
}

//  void QQStyleKitControls::set_busyIndicator(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17set_busyIndicatorEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_busyIndicator(control);
}

//  void QQStyleKitControls::set_button(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls10set_buttonEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_button(control);
}

//  void QQStyleKitControls::set_checkBox(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls12set_checkBoxEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_checkBox(control);
}

//  void QQStyleKitControls::set_checkDelegate(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17set_checkDelegateEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_checkDelegate(control);
}

//  void QQStyleKitControls::set_comboBox(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls12set_comboBoxEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_comboBox(control);
}

//  void QQStyleKitControls::set_delayButton(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls15set_delayButtonEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_delayButton(control);
}

//  void QQStyleKitControls::set_dial(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls8set_dialEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_dial(control);
}

//  void QQStyleKitControls::set_dialog(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls10set_dialogEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_dialog(control);
}

//  void QQStyleKitControls::set_dialogButtonBox(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls19set_dialogButtonBoxEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_dialogButtonBox(control);
}

//  void QQStyleKitControls::set_flatButton(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls14set_flatButtonEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_flatButton(control);
}

//  void QQStyleKitControls::set_progressBar(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls15set_progressBarEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_progressBar(control);
}

//  void QQStyleKitControls::set_scrollBar(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls13set_scrollBarEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_scrollBar(control);
}

//  void QQStyleKitControls::set_scrollIndicator(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls19set_scrollIndicatorEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_scrollIndicator(control);
}

//  void QQStyleKitControls::set_scrollView(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls14set_scrollViewEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_scrollView(control);
}

//  void QQStyleKitControls::set_searchField(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls15set_searchFieldEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_searchField(control);
}

//  void QQStyleKitControls::set_slider(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls10set_sliderEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_slider(control);
}

//  void QQStyleKitControls::set_spinBox(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls11set_spinBoxEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_spinBox(control);
}

//  void QQStyleKitControls::set_tabBar(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls10set_tabBarEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_tabBar(control);
}

//  void QQStyleKitControls::set_tabButton(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls13set_tabButtonEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_tabButton(control);
}

//  void QQStyleKitControls::set_textField(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls13set_textFieldEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_textField(control);
}

//  void QQStyleKitControls::set_textInput(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls13set_textInputEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_textInput(control);
}

//  void QQStyleKitControls::set_toolBar(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls11set_toolBarEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_toolBar(control);
}

//  void QQStyleKitControls::set_toolButton(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls14set_toolButtonEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_toolButton(control);
}

//  void QQStyleKitControls::set_toolSeparator(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17set_toolSeparatorEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_toolSeparator(control);
}

//  void QQStyleKitControls::set_swipeDelegate(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17set_swipeDelegateEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_swipeDelegate(control);
}

//  void QQStyleKitControls::set_switchControl(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17set_switchControlEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_switchControl(control);
}

//  void QQStyleKitControls::set_switchDelegate(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls18set_switchDelegateEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_switchDelegate(control);
}

//  void QQStyleKitControls::set_radioButton(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls15set_radioButtonEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_radioButton(control);
}

//  void QQStyleKitControls::set_radioDelegate(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17set_radioDelegateEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_radioDelegate(control);
}

//  void QQStyleKitControls::set_roundButton(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls15set_roundButtonEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_roundButton(control);
}

//  void QQStyleKitControls::set_itemDelegate(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls16set_itemDelegateEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_itemDelegate(control);
}

//  void QQStyleKitControls::set_popup(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls9set_popupEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_popup(control);
}

//  void QQStyleKitControls::set_pane(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls8set_paneEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_pane(control);
}

//  void QQStyleKitControls::set_page(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls8set_pageEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_page(control);
}

//  void QQStyleKitControls::set_pageIndicator(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17set_pageIndicatorEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_pageIndicator(control);
}

//  void QQStyleKitControls::set_frame(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls9set_frameEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_frame(control);
}

//  void QQStyleKitControls::set_label(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls9set_labelEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_label(control);
}

//  void QQStyleKitControls::set_groupBox(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls12set_groupBoxEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_groupBox(control);
}

//  void QQStyleKitControls::set_textArea(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls12set_textAreaEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_textArea(control);
}

//  void QQStyleKitControls::set_menu(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls8set_menuEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_menu(control);
}

//  void QQStyleKitControls::set_menuBar(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls11set_menuBarEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_menuBar(control);
}

//  void QQStyleKitControls::set_menuBarItem(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls15set_menuBarItemEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_menuBarItem(control);
}

//  void QQStyleKitControls::set_menuItem(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls12set_menuItemEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_menuItem(control);
}

//  void QQStyleKitControls::set_menuSeparator(QQStyleKitControl *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17set_menuSeparatorEP17QQStyleKitControl(
    QQStyleKitControls *self,
    QQStyleKitControl *control) {
  self->set_menuSeparator(control);
}

//  QQStyleKitControl
//      *QQStyleKitControls::getControlStyle(QQStyleKitExtendableControlType
//      controlType) const
extern "C" Q_DECL_EXPORT
QQStyleKitControl *ritual_ZNK18QQStyleKitControls15getControlStyleEj(
    const QQStyleKitControls *self,
    QQStyleKitExtendableControlType controlType) {
  return self->getControlStyle(controlType);
}

//  QQmlListProperty<QObject> QQStyleKitControls::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN18QQStyleKitControls4dataEv(
    QQStyleKitControls *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  const QList<QObject *> QQStyleKitControls::children() const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK18QQStyleKitControls8childrenEv(
    const QQStyleKitControls *self) {
  return new QList<QObject *>(self->children());
}

//  void QQStyleKitControls::dataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls11dataChangedEv(QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dataChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dataChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::applicationWindowChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls24applicationWindowChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "applicationWindowChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "applicationWindowChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::abstractButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls21abstractButtonChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "abstractButtonChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "abstractButtonChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::controlChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls14controlChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "controlChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "controlChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::busyIndicatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls20busyIndicatorChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "busyIndicatorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "busyIndicatorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::buttonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls13buttonChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "buttonChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "buttonChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::checkBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls15checkBoxChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "checkBoxChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "checkBoxChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::checkDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls20checkDelegateChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "checkDelegateChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "checkDelegateChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::comboBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls15comboBoxChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "comboBoxChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "comboBoxChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::delayButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls18delayButtonChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "delayButtonChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "delayButtonChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::dialChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls11dialChangedEv(QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dialChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dialChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::dialogChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls13dialogChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dialogChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dialogChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::dialogButtonBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls22dialogButtonBoxChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dialogButtonBoxChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dialogButtonBoxChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::flatButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17flatButtonChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "flatButtonChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "flatButtonChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::progressBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls18progressBarChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "progressBarChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "progressBarChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::scrollBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls16scrollBarChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "scrollBarChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "scrollBarChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::scrollIndicatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls22scrollIndicatorChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "scrollIndicatorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "scrollIndicatorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::scrollViewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17scrollViewChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "scrollViewChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "scrollViewChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::searchFieldChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls18searchFieldChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "searchFieldChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "searchFieldChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::sliderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls13sliderChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sliderChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sliderChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::spinBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls14spinBoxChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "spinBoxChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "spinBoxChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::tabBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls13tabBarChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tabBarChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tabBarChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::tabButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls16tabButtonChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tabButtonChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tabButtonChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::textFieldChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls16textFieldChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textFieldChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textFieldChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::textInputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls16textInputChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textInputChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textInputChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::toolBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls14toolBarChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "toolBarChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "toolBarChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::toolButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17toolButtonChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "toolButtonChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "toolButtonChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::toolSeparatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls20toolSeparatorChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "toolSeparatorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "toolSeparatorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::swipeDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls20swipeDelegateChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "swipeDelegateChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "swipeDelegateChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::switchControlChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls20switchControlChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "switchControlChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "switchControlChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::switchDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls21switchDelegateChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "switchDelegateChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "switchDelegateChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::radioButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls18radioButtonChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "radioButtonChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "radioButtonChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::radioDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls20radioDelegateChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "radioDelegateChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "radioDelegateChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::roundButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls18roundButtonChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "roundButtonChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "roundButtonChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::itemDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls19itemDelegateChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "itemDelegateChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "itemDelegateChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::popupChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls12popupChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "popupChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "popupChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::paneChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls11paneChangedEv(QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "paneChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "paneChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::pageChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls11pageChangedEv(QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pageChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pageChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::pageIndicatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls20pageIndicatorChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pageIndicatorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pageIndicatorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::frameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls12frameChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "frameChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "frameChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::labelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls12labelChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "labelChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "labelChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::groupBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls15groupBoxChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "groupBoxChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "groupBoxChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::textAreaChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls15textAreaChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textAreaChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textAreaChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::menuChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls11menuChangedEv(QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "menuChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "menuChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::menuBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls14menuBarChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "menuBarChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "menuBarChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::menuBarItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls18menuBarItemChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "menuBarItemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "menuBarItemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::menuItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls15menuItemChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "menuItemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "menuItemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::menuSeparatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls20menuSeparatorChangedEv(
    QQStyleKitControls *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitControls")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "menuSeparatorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "menuSeparatorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitControls::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls10classBeginEv(QQStyleKitControls *self) {
  self->classBegin();
}

//  void QQStyleKitControls::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17componentCompleteEv(
    QQStyleKitControls *self) {
  self->componentComplete();
}

//  QQStyleKitControls as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQStyleKitControls_QQmlParserStatus(
    QQStyleKitControls *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QQStyleKitControls::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQStyleKitControls10classBeginEv(
    QQStyleKitControls *self) {
  static_cast<OwnQQStyleKitControls *>(self)->OwnQQStyleKitControls::classBegin();
}

//  a QQmlListProperty<QObject> a ritual of QQStyleKitControls gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQStyleKitControls__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
