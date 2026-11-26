//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command2_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/qdesigner_command2_p.h>
#include <QtDesigner/private/formwindowbase_p.h>
#include <QtDesigner/private/layoutinfo_p.h>
#include <QtDesigner/private/qdesigner_command_p.h>
#include <QtDesigner/private/widgetfactory_p.h>
#include <QtDesigner/private/qlayout_widget_p.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/abstractmetadatabase.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qlayout.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command2.cpp, line 120, as _ZN18qdesigner_internal22LayoutAlignmentCommandC1EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
inline LayoutAlignmentCommand::LayoutAlignmentCommand(QDesignerFormWindowInterface *formWindow) :
    QDesignerFormWindowCommand(QApplication::translate("Command", "Change layout alignment"), formWindow),
    m_widget(nullptr)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command2.cpp, line 126, as _ZN18qdesigner_internal22LayoutAlignmentCommand4initEP7QWidget6QFlagsIN2Qt13AlignmentFlagEE
namespace qdesigner_internal {
inline bool LayoutAlignmentCommand::init(QWidget *w, Qt::Alignment alignment)
{
    bool enabled;
    m_newAlignment = alignment;
    m_oldAlignment = LayoutAlignmentCommand::alignmentOf(core(), w, &enabled);
    m_widget = w;
    return enabled;
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command2.cpp, line 135, as _ZN18qdesigner_internal22LayoutAlignmentCommand4redoEv
namespace qdesigner_internal {
inline void LayoutAlignmentCommand::redo()
{
    LayoutAlignmentCommand::applyAlignment(core(), m_widget, m_newAlignment);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command2.cpp, line 140, as _ZN18qdesigner_internal22LayoutAlignmentCommand4undoEv
namespace qdesigner_internal {
inline void LayoutAlignmentCommand::undo()
{
    LayoutAlignmentCommand::applyAlignment(core(), m_widget, m_oldAlignment);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command2.cpp, line 146, as _ZN18qdesigner_internal22LayoutAlignmentCommand11alignmentOfEPK28QDesignerFormEditorInterfaceP7QWidgetPb
namespace qdesigner_internal {
inline Qt::Alignment LayoutAlignmentCommand::alignmentOf(const QDesignerFormEditorInterface *core, QWidget *w, bool *enabledIn)
{
    bool managed;
    QLayout *layout;

    if (enabledIn)
        *enabledIn = false;
    // Can only work on a managed layout
    const LayoutInfo::Type type = LayoutInfo::laidoutWidgetType(core, w, &managed, &layout);
    const bool enabled = layout && managed &&
                         (type == LayoutInfo::HBox || type == LayoutInfo::VBox
                          || type == LayoutInfo::Grid);
    if (!enabled)
        return {};
    // Get alignment
    const int index = layout->indexOf(w);
    Q_ASSERT(index >= 0);
    if (enabledIn)
        *enabledIn = true;
    return layout->itemAt(index)->alignment();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command2.cpp, line 168, as _ZN18qdesigner_internal22LayoutAlignmentCommand14applyAlignmentEPK28QDesignerFormEditorInterfaceP7QWidget6QFlagsIN2Qt13AlignmentFlagEE
namespace qdesigner_internal {
inline void LayoutAlignmentCommand::applyAlignment(const QDesignerFormEditorInterface *core, QWidget *w, Qt::Alignment a)
{
    // Find layout and apply to item
    QLayout *layout;
    LayoutInfo::laidoutWidgetType(core, w, nullptr, &layout);
    if (layout) {
        const int index = layout->indexOf(w);
        if (index >= 0) {
            layout->itemAt(index)->setAlignment(a);
            layout->update();
        }
    }
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  qdesigner_internal::LayoutAlignmentCommand::LayoutAlignmentCommand(QDesig
//      nerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::LayoutAlignmentCommand *ritual_ZN18qdesigner_internal22LayoutAlignmentCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::LayoutAlignmentCommand(formWindow);
}

//  bool qdesigner_internal::LayoutAlignmentCommand::init(QWidget *w,
//      Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal22LayoutAlignmentCommand4initEP7QWidget6QFlagsIN2Qt13AlignmentFlagEE(
    qdesigner_internal::LayoutAlignmentCommand *self,
    QWidget *w,
    int alignment) {
  return self->init(w, QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void qdesigner_internal::LayoutAlignmentCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22LayoutAlignmentCommand4redoEv(
    qdesigner_internal::LayoutAlignmentCommand *self) {
  self->redo();
}

//  void qdesigner_internal::LayoutAlignmentCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22LayoutAlignmentCommand4undoEv(
    qdesigner_internal::LayoutAlignmentCommand *self) {
  self->undo();
}

//  Qt::Alignment
//      qdesigner_internal::LayoutAlignmentCommand::alignmentOf(const
//      QDesignerFormEditorInterface *core, QWidget *w, bool *enabled)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal22LayoutAlignmentCommand11alignmentOfEPK28QDesignerFormEditorInterfaceP7QWidgetPb(
    const QDesignerFormEditorInterface *core,
    QWidget *w,
    bool *enabled) {
  return static_cast<int>(
      qdesigner_internal::LayoutAlignmentCommand::alignmentOf(
          core,
          w,
          enabled).toInt());
}

//  void qdesigner_internal::LayoutAlignmentCommand::applyAlignment(const
//      QDesignerFormEditorInterface *core, QWidget *w, Qt::Alignment a)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22LayoutAlignmentCommand14applyAlignmentEPK28QDesignerFormEditorInterfaceP7QWidget6QFlagsIN2Qt13AlignmentFlagEE(
    const QDesignerFormEditorInterface *core,
    QWidget *w,
    int a) {
  qdesigner_internal::LayoutAlignmentCommand::applyAlignment(
      core,
      w,
      QFlags<Qt::AlignmentFlag>::fromInt(a));
}

//  void qdesigner_internal::LayoutAlignmentCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal22LayoutAlignmentCommand4redoEv(
    qdesigner_internal::LayoutAlignmentCommand *self) {
  self->qdesigner_internal::LayoutAlignmentCommand::redo();
}

//  void qdesigner_internal::LayoutAlignmentCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal22LayoutAlignmentCommand4undoEv(
    qdesigner_internal::LayoutAlignmentCommand *self) {
  self->qdesigner_internal::LayoutAlignmentCommand::undo();
}
