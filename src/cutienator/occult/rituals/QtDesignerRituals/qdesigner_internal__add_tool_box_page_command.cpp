//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/qdesigner_command_p.h>
#include <QtDesigner/private/qdesigner_utils_p.h>
#include <QtDesigner/private/layout_p.h>
#include <QtDesigner/private/qlayout_widget_p.h>
#include <QtDesigner/private/qdesigner_widget_p.h>
#include <QtDesigner/private/qdesigner_menu_p.h>
#include <QtDesigner/private/shared_enums_p.h>
#include <QtDesigner/private/metadatabase_p.h>
#include <QtDesigner/private/formwindowbase_p.h>
#include <QtDesigner/abstractformbuilder.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/propertysheet.h>
#include <QtDesigner/abstractactioneditor.h>
#include <QtDesigner/abstractpropertyeditor.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtDesigner/container.h>
#include <QtDesigner/layoutdecoration.h>
#include <QtDesigner/abstractwidgetfactory.h>
#include <QtDesigner/abstractobjectinspector.h>
#include <QtDesigner/abstractintegration.h>
#include <QtDesigner/abstractformwindowcursor.h>
#include <QtCore/qdebug.h>
#include <QtCore/qtextstream.h>
#include <QtCore/qqueue.h>
#include <QtWidgets/qmenubar.h>
#include <QtWidgets/qstatusbar.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/qtoolbox.h>
#include <QtWidgets/qstackedwidget.h>
#include <QtWidgets/qtabwidget.h>
#include <QtWidgets/qtablewidget.h>
#include <QtWidgets/qtreewidget.h>
#include <QtWidgets/qlistwidget.h>
#include <QtWidgets/qcombobox.h>
#include <QtWidgets/qsplitter.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/qwizard.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qformlayout.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 928, as _ZN18qdesigner_internal14ToolBoxCommandC2EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline ToolBoxCommand::ToolBoxCommand(QDesignerFormWindowInterface *formWindow)  :
    QDesignerFormWindowCommand(QString(), formWindow),
    m_index(-1)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1065, as _ZN18qdesigner_internal21AddToolBoxPageCommand4redoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void AddToolBoxPageCommand::redo()
{
    addPage();
    cheapUpdate();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1071, as _ZN18qdesigner_internal21AddToolBoxPageCommand4undoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void AddToolBoxPageCommand::undo()
{
    removePage();
    cheapUpdate();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1039, as _ZN18qdesigner_internal21AddToolBoxPageCommandD2Ev
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline AddToolBoxPageCommand::~AddToolBoxPageCommand() = default;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 945, as _ZN18qdesigner_internal14ToolBoxCommand10removePageEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ToolBoxCommand::removePage()
{
    m_toolBox->removeItem(m_index);

    m_widget->hide();
    m_widget->setParent(formWindow());
    formWindow()->clearSelection();
    formWindow()->selectWidget(m_toolBox, true);

}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 956, as _ZN18qdesigner_internal14ToolBoxCommand7addPageEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ToolBoxCommand::addPage()
{
    m_widget->setParent(m_toolBox);
    m_toolBox->insertItem(m_index, m_widget, m_itemIcon, m_itemText);
    m_toolBox->setCurrentIndex(m_index);

    QDesignerPropertySheetExtension *sheet = qt_extension<QDesignerPropertySheetExtension*>(formWindow()->core()->extensionManager(), m_toolBox);
    if (sheet) {
        qdesigner_internal::PropertySheetStringValue itemText(m_itemText);
        sheet->setProperty(sheet->indexOf(u"currentItemText"_s), QVariant::fromValue(itemText));
    }

    m_widget->show();
    formWindow()->clearSelection();
    formWindow()->selectWidget(m_toolBox, true);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 934, as _ZN18qdesigner_internal14ToolBoxCommandD2Ev
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline ToolBoxCommand::~ToolBoxCommand() = default;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1034, as _ZN18qdesigner_internal21AddToolBoxPageCommandC1EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline AddToolBoxPageCommand::AddToolBoxPageCommand(QDesignerFormWindowInterface *formWindow)
    : ToolBoxCommand(formWindow)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1041, as _ZN18qdesigner_internal21AddToolBoxPageCommand4initEP8QToolBox
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void AddToolBoxPageCommand::init(QToolBox *toolBox)
{
    init(toolBox, InsertBefore);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1046, as _ZN18qdesigner_internal21AddToolBoxPageCommand4initEP8QToolBoxNS0_13InsertionModeE
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void AddToolBoxPageCommand::init(QToolBox *toolBox, InsertionMode mode)
{
    m_toolBox = toolBox;

    m_index = m_toolBox->currentIndex();
    if (mode == InsertAfter)
        m_index++;
    m_widget = new QDesignerWidget(formWindow(), m_toolBox);
    m_itemText = QApplication::translate("Command", "Page");
    m_itemIcon = QIcon();
    m_widget->setObjectName(u"page"_s);
    formWindow()->ensureUniqueObjectName(m_widget);

    setText(QApplication::translate("Command", "Insert Page"));

    QDesignerFormEditorInterface *core = formWindow()->core();
    core->metaDataBase()->add(m_widget);
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  A qdesigner_internal::AddToolBoxPageCommand that Python can take functions over in. Every qdesigner_internal::AddToolBoxPageCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_AddToolBoxPageCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_AddToolBoxPageCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_AddToolBoxPageCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_AddToolBoxPageCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_AddToolBoxPageCommand : public qdesigner_internal::AddToolBoxPageCommand {
public:
  using qdesigner_internal::AddToolBoxPageCommand::AddToolBoxPageCommand;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4redoEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4undoEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZNK12QUndoCommand2idEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand9mergeWithEPKS_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
    return false;
  }

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::AddToolBoxPageCommand::redo()
  void redo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_AddToolBoxPageCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_AddToolBoxPageCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::AddToolBoxPageCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::AddToolBoxPageCommand::undo()
  void undo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_AddToolBoxPageCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_AddToolBoxPageCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::AddToolBoxPageCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_AddToolBoxPageCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_AddToolBoxPageCommandCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QUndoCommand::id();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  bool QUndoCommand::mergeWith(const QUndoCommand *other)
  bool mergeWith(const QUndoCommand *other) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_AddToolBoxPageCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_AddToolBoxPageCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  qdesigner_internal::AddToolBoxPageCommand::AddToolBoxPageCommand(QDesigne
//      rFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::AddToolBoxPageCommand *ritual_ZN18qdesigner_internal21AddToolBoxPageCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new Cuteqdesigner_internal_AddToolBoxPageCommand(formWindow);
}

//  qdesigner_internal::AddToolBoxPageCommand::~AddToolBoxPageCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21AddToolBoxPageCommandD1Ev(
    qdesigner_internal::AddToolBoxPageCommand *self) {
  delete self;
}

//  void qdesigner_internal::AddToolBoxPageCommand::init(QToolBox *toolBox)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21AddToolBoxPageCommand4initEP8QToolBox(
    qdesigner_internal::AddToolBoxPageCommand *self,
    QToolBox *toolBox) {
  self->init(toolBox);
}

//  void qdesigner_internal::AddToolBoxPageCommand::init(QToolBox *toolBox,
//      InsertionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21AddToolBoxPageCommand4initEP8QToolBoxNS0_13InsertionModeE(
    qdesigner_internal::AddToolBoxPageCommand *self,
    QToolBox *toolBox,
    qdesigner_internal::AddToolBoxPageCommand::InsertionMode mode) {
  self->init(toolBox, mode);
}

//  void qdesigner_internal::AddToolBoxPageCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21AddToolBoxPageCommand4redoEv(
    qdesigner_internal::AddToolBoxPageCommand *self) {
  self->redo();
}

//  void qdesigner_internal::AddToolBoxPageCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21AddToolBoxPageCommand4undoEv(
    qdesigner_internal::AddToolBoxPageCommand *self) {
  self->undo();
}

//  a Python function taken by a
//      Cuteqdesigner_internal_AddToolBoxPageCommand, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_AddToolBoxPageCommand(
    qdesigner_internal::AddToolBoxPageCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_AddToolBoxPageCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::AddToolBoxPageCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal21AddToolBoxPageCommand4redoEv(
    qdesigner_internal::AddToolBoxPageCommand *self) {
  self->qdesigner_internal::AddToolBoxPageCommand::redo();
}

//  void qdesigner_internal::AddToolBoxPageCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal21AddToolBoxPageCommand4undoEv(
    qdesigner_internal::AddToolBoxPageCommand *self) {
  self->qdesigner_internal::AddToolBoxPageCommand::undo();
}
