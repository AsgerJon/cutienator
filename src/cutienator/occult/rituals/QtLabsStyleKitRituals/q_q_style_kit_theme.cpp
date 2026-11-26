//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekittheme_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekittheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquicktheme_p.h>
#include <QtQuick/private/qquickpalette_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyleandthemebase_p.h>
#include <QtLabsStyleKit/private/qqstylekitvariation_p.h>
#include <QtLabsStyleKit/private/qqstylekitpalette_p.h>
#include <QtLabsStyleKit/private/qqstylekitfont_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h>
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

//  from ../qtdeclarative/src/labs/stylekit/qqstylekittheme.cpp, line 50, as local:qqstylekittheme.cpp:scopeForType
static QQuickTheme::Scope scopeForType(QQStyleKitExtendableControlType type)
{
    switch (type) {
    case QQStyleKitReader::ControlType::AbstractButton:
    case QQStyleKitReader::ControlType::Button:
    case QQStyleKitReader::ControlType::DelayButton:
    case QQStyleKitReader::ControlType::FlatButton:
    case QQStyleKitReader::ControlType::RoundButton:
        return QQuickTheme::Button;
    case QQStyleKitReader::ControlType::CheckBox:
        return QQuickTheme::CheckBox;
    case QQStyleKitReader::ControlType::CheckDelegate:
    case QQStyleKitReader::ControlType::RadioDelegate:
    case QQStyleKitReader::ControlType::SwipeDelegate:
    case QQStyleKitReader::ControlType::SwitchDelegate:
        return QQuickTheme::ListView;
    case QQStyleKitReader::ControlType::ComboBox:
        return QQuickTheme::ComboBox;
    case QQStyleKitReader::ControlType::GroupBox:
        return QQuickTheme::GroupBox;
    case QQStyleKitReader::ControlType::ItemDelegate:
        return QQuickTheme::ItemView;
    case QQStyleKitReader::ControlType::Label:
        return QQuickTheme::Label;
    case QQStyleKitReader::ControlType::MenuBar:
    case QQStyleKitReader::ControlType::MenuBarItem:
        return QQuickTheme::MenuBar;
    case QQStyleKitReader::ControlType::Menu:
    case QQStyleKitReader::ControlType::MenuItem:
    case QQStyleKitReader::ControlType::MenuSeparator:
        return QQuickTheme::Menu;
    case QQStyleKitReader::ControlType::RadioButton:
        return QQuickTheme::RadioButton;
    case QQStyleKitReader::ControlType::SpinBox:
        return QQuickTheme::SpinBox;
    case QQStyleKitReader::ControlType::SwitchControl:
        return QQuickTheme::Switch;
    case QQStyleKitReader::ControlType::TabBar:
    case QQStyleKitReader::ControlType::TabButton:
        return QQuickTheme::TabBar;
    case QQStyleKitReader::ControlType::TextArea:
        return QQuickTheme::TextArea;
    case QQStyleKitReader::ControlType::TextInput:
    case QQStyleKitReader::ControlType::TextField:
        return QQuickTheme::TextField;
    case QQStyleKitReader::ControlType::ToolBar:
    case QQStyleKitReader::ControlType::ToolButton:
    case QQStyleKitReader::ControlType::ToolSeparator:
        return QQuickTheme::ToolBar;
    default:
        return QQuickTheme::System;
    }
    Q_UNREACHABLE();
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekittheme.cpp, line 221, as _ZN15QQStyleKitTheme17componentCompleteEv
inline void QQStyleKitTheme::componentComplete()
{
    QQStyleKitControls::componentComplete();
    m_completed = true;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitstyleandthemebase.cpp, line 21, as _ZN27QQStyleKitStyleAndThemeBaseC2EP7QObject
inline QQStyleKitStyleAndThemeBase::QQStyleKitStyleAndThemeBase(QObject *parent)
    : QQStyleKitControls(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitstyleandthemebase.cpp, line 67, as _ZN27QQStyleKitStyleAndThemeBase8palettesEv
inline QQStyleKitPalette *QQStyleKitStyleAndThemeBase::palettes()
{
    return &m_palettes;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 35, as _ZNK17QQStyleKitPalette11radioButtonEv
inline QQuickPalette *QQStyleKitPalette::radioButton() const { if (!m_radioButton) { m_radioButton.reset(new QQuickPalette()); QObject::connect(m_radioButton.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::RadioButton); emit self->radioButtonChanged(); }); } return m_radioButton.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 33, as _ZNK17QQStyleKitPalette12itemDelegateEv
inline QQuickPalette *QQStyleKitPalette::itemDelegate() const { if (!m_itemDelegate) { m_itemDelegate.reset(new QQuickPalette()); QObject::connect(m_itemDelegate.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::ItemView); emit self->itemDelegateChanged(); }); } return m_itemDelegate.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 43, as _ZNK17QQStyleKitPalette15fallbackPaletteEv
inline QQStyleKitPalette *QQStyleKitPalette::fallbackPalette() const
{
    return m_fallbackPalette;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 34, as _ZNK17QQStyleKitPalette5labelEv
inline QQuickPalette *QQStyleKitPalette::label() const { if (!m_label) { m_label.reset(new QQuickPalette()); QObject::connect(m_label.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::Label); emit self->labelChanged(); }); } return m_label.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 30, as _ZNK17QQStyleKitPalette6buttonEv
inline QQuickPalette *QQStyleKitPalette::button() const { if (!m_button) { m_button.reset(new QQuickPalette()); QObject::connect(m_button.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::Button); emit self->buttonChanged(); }); } return m_button.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 28, as _ZNK17QQStyleKitPalette6systemEv
inline QQuickPalette *QQStyleKitPalette::system() const { if (!m_system) { m_system.reset(new QQuickPalette()); QObject::connect(m_system.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::System); emit self->systemChanged(); }); } return m_system.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 38, as _ZNK17QQStyleKitPalette6tabBarEv
inline QQuickPalette *QQStyleKitPalette::tabBar() const { if (!m_tabBar) { m_tabBar.reset(new QQuickPalette()); QObject::connect(m_tabBar.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::TabBar); emit self->tabBarChanged(); }); } return m_tabBar.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 36, as _ZNK17QQStyleKitPalette7spinBoxEv
inline QQuickPalette *QQStyleKitPalette::spinBox() const { if (!m_spinBox) { m_spinBox.reset(new QQuickPalette()); QObject::connect(m_spinBox.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::SpinBox); emit self->spinBoxChanged(); }); } return m_spinBox.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 41, as _ZNK17QQStyleKitPalette7toolBarEv
inline QQuickPalette *QQStyleKitPalette::toolBar() const { if (!m_toolBar) { m_toolBar.reset(new QQuickPalette()); QObject::connect(m_toolBar.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::ToolBar); emit self->toolBarChanged(); }); } return m_toolBar.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 29, as _ZNK17QQStyleKitPalette8checkBoxEv
inline QQuickPalette *QQStyleKitPalette::checkBox() const { if (!m_checkBox) { m_checkBox.reset(new QQuickPalette()); QObject::connect(m_checkBox.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::CheckBox); emit self->checkBoxChanged(); }); } return m_checkBox.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 31, as _ZNK17QQStyleKitPalette8comboBoxEv
inline QQuickPalette *QQStyleKitPalette::comboBox() const { if (!m_comboBox) { m_comboBox.reset(new QQuickPalette()); QObject::connect(m_comboBox.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::ComboBox); emit self->comboBoxChanged(); }); } return m_comboBox.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 32, as _ZNK17QQStyleKitPalette8groupBoxEv
inline QQuickPalette *QQStyleKitPalette::groupBox() const { if (!m_groupBox) { m_groupBox.reset(new QQuickPalette()); QObject::connect(m_groupBox.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::GroupBox); emit self->groupBoxChanged(); }); } return m_groupBox.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 39, as _ZNK17QQStyleKitPalette8textAreaEv
inline QQuickPalette *QQStyleKitPalette::textArea() const { if (!m_textArea) { m_textArea.reset(new QQuickPalette()); QObject::connect(m_textArea.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::TextArea); emit self->textAreaChanged(); }); } return m_textArea.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 40, as _ZNK17QQStyleKitPalette9textFieldEv
inline QQuickPalette *QQStyleKitPalette::textField() const { if (!m_textField) { m_textField.reset(new QQuickPalette()); QObject::connect(m_textField.get(), &QQuickPalette::changed, const_cast<QQStyleKitPalette*>(this), [this]() { auto *self = const_cast<QQStyleKitPalette*>(this); self->markSet(QQuickTheme::TextField); emit self->textFieldChanged(); }); } return m_textField.get(); }

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitstyleandthemebase.cpp, line 43, as _ZN27QQStyleKitStyleAndThemeBase5fontsEv
inline QQStyleKitFont *QQStyleKitStyleAndThemeBase::fonts()
{
    return &m_fonts;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 69, as _ZNK14QQStyleKitFont12fallbackFontEv
inline QQStyleKitFont *QQStyleKitFont::fallbackFont() const
{
    return m_fallback;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 83, as _ZNK14QQStyleKitFont12fontForScopeEN11QQuickTheme5ScopeE
inline QFont QQStyleKitFont::fontForScope(QQuickTheme::Scope scope) const
{
    return m_fonts[int(scope)];
}

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

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 614, as _ZNK18QQStyleKitControls8childrenEv
inline const QList<QObject *> QQStyleKitControls::children() const
{
    return m_data;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcustomcontrol.cpp, line 67, as _ZNK23QQStyleKitCustomControl11controlTypeEv
inline int QQStyleKitCustomControl::controlType() const
{
    return m_controlType;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekittheme.cpp, line 110, as _ZNK15QQStyleKitTheme5styleEv
inline QQStyleKitStyle *QQStyleKitTheme::style() const
{
    QObject *parentObj = parent();
    if (!parentObj)
        return nullptr;
    Q_ASSERT(qobject_cast<QQStyleKitStyle *>(parentObj));
    return static_cast<QQStyleKitStyle *>(parentObj);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekittheme.cpp, line 119, as _ZNK15QQStyleKitTheme21paletteForControlTypeEj
inline QPalette QQStyleKitTheme::paletteForControlType(QQStyleKitExtendableControlType type) const
{
    const QQuickTheme::Scope scope = scopeForType(type);
    return m_effectivePalettes[int(scope)];
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekittheme.cpp, line 131, as _ZN15QQStyleKitTheme19updateThemePalettesEv
inline void QQStyleKitTheme::updateThemePalettes()
{
    const QQStyleKitPalette *pals = palettes();
    if (!pals)
        return;

    // Collect palette fallback chain
    QVector<const QQStyleKitPalette *> fbChain;
    for (auto *fb = pals; fb; fb = fb->fallbackPalette())
        fbChain.append(fb);

    auto resolveFromPaletteChain = [&](QQuickTheme::Scope scope,
        QQuickPalette* (QQStyleKitPalette::*getter)() const) -> QPalette
    {
        QPalette result;

        // Apply from farthest fallback -> local
        for (int i = fbChain.size() - 1; i >= 0; --i) {
            const QQStyleKitPalette *fb = fbChain[i];
            // Apply system palette first as a base, and override with scope-specific palette
            if (scope != QQuickTheme::System && fb->isSet(QQuickTheme::System)) {
                if (auto *sys = fb->system())
                    result = sys->toQPalette().resolve(result);
            }
            if (fb->isSet(scope)) {
                if (auto *p = (fb->*getter)())
                    result = p->toQPalette().resolve(result);
            }
        }

        return result;
    };

    auto setResolved = [&](QQuickPalette* (QQStyleKitPalette::*getter)() const,
        QQuickTheme::Scope scope)
    {
        m_effectivePalettes[int(scope)] = resolveFromPaletteChain(scope, getter);
    };

    setResolved(&QQStyleKitPalette::system, QQuickTheme::System);
    setResolved(&QQStyleKitPalette::button, QQuickTheme::Button);
    setResolved(&QQStyleKitPalette::checkBox, QQuickTheme::CheckBox);
    setResolved(&QQStyleKitPalette::comboBox, QQuickTheme::ComboBox);
    setResolved(&QQStyleKitPalette::groupBox, QQuickTheme::GroupBox);
    setResolved(&QQStyleKitPalette::itemDelegate, QQuickTheme::ItemView);
    setResolved(&QQStyleKitPalette::label, QQuickTheme::Label);
    setResolved(&QQStyleKitPalette::radioButton, QQuickTheme::RadioButton);
    setResolved(&QQStyleKitPalette::spinBox, QQuickTheme::SpinBox);
    setResolved(&QQStyleKitPalette::tabBar, QQuickTheme::TabBar);
    setResolved(&QQStyleKitPalette::textArea, QQuickTheme::TextArea);
    setResolved(&QQStyleKitPalette::textField, QQuickTheme::TextField);
    setResolved(&QQStyleKitPalette::toolBar, QQuickTheme::ToolBar);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekittheme.cpp, line 185, as _ZN15QQStyleKitTheme16updateThemeFontsEv
inline void QQStyleKitTheme::updateThemeFonts()
{
    const QQStyleKitFont *fonts = this->fonts();
    if (!fonts)
        return;

    // Collect font fallback chain
    QVector<const QQStyleKitFont *> fbChain;
    for (auto *fb = fonts; fb; fb = fb->fallbackFont())
        fbChain.append(fb);

    auto resolveFromFontChain = [&](QQuickTheme::Scope scope) -> QFont
    {
        QFont result;

        // Apply from farthest fallback -> local
        for (int i = fbChain.size() - 1; i >= 0; --i) {
            const QQStyleKitFont *fb = fbChain[i];
            // Apply system font first as a base, and override with scope-specific font
            if (scope != QQuickTheme::System && fb->isSet(QQuickTheme::System)) {
                result = fb->fontForScope(QQuickTheme::System).resolve(result);
            }
            if (fb->isSet(scope)) {
                result = fb->fontForScope(scope).resolve(result);
            }
        }

        return result;
    };

    for (int i = 0; i < NScopes; ++i) {
        const QQuickTheme::Scope scope = static_cast<QQuickTheme::Scope>(i);
        m_effectiveFonts[i] = resolveFromFontChain(scope);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QQStyleKitTheme may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQStyleKitTheme : QQStyleKitTheme {
  using QQStyleKitTheme::componentComplete;
};

//  const QMetaObject *QQStyleKitTheme::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQStyleKitTheme10metaObjectEv(
    const QQStyleKitTheme *self) {
  return self->metaObject();
}

//  void *QQStyleKitTheme::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQStyleKitTheme11qt_metacastEPKc(
    QQStyleKitTheme *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitTheme::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQStyleKitTheme11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitTheme *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQStyleKitStyle *QQStyleKitTheme::style() const
extern "C" Q_DECL_EXPORT
QQStyleKitStyle *ritual_ZNK15QQStyleKitTheme5styleEv(
    const QQStyleKitTheme *self) {
  return self->style();
}

//  QPalette
//      QQStyleKitTheme::paletteForControlType(QQStyleKitExtendableControlTyp
//      e type) const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK15QQStyleKitTheme21paletteForControlTypeEj(
    const QQStyleKitTheme *self,
    QQStyleKitExtendableControlType type) {
  return new QPalette(self->paletteForControlType(type));
}

//  void QQStyleKitTheme::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitTheme17componentCompleteEv(QQStyleKitTheme *self) {
  self->componentComplete();
}

//  void QQStyleKitTheme::updateThemePalettes()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitTheme19updateThemePalettesEv(
    QQStyleKitTheme *self) {
  self->updateThemePalettes();
}

//  void QQStyleKitTheme::updateThemeFonts()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitTheme16updateThemeFontsEv(QQStyleKitTheme *self) {
  self->updateThemeFonts();
}
