//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/signalslotdialog_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/signalslotdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/signalslotdialog_p.h>
#include <QtDesigner/private/metadatabase_p.h>
#include <QtDesigner/private/widgetdatabase_p.h>
#include <QtDesigner/private/qdesigner_formwindowcommand_p.h>
#include <QtDesigner/private/iconloader_p.h>
#include <QtDesigner/membersheet.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractwidgetfactory.h>
#include <QtDesigner/private/abstractdialoggui_p.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtGui/qvalidator.h>
#include <QtWidgets/qstyleditemdelegate.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qmessagebox.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 153, as _ZN18qdesigner_internal20SignalSlotDialogData5clearEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void SignalSlotDialogData::clear()
{
    m_existingMethods.clear();
    m_fakeMethods.clear();
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  void qdesigner_internal::SignalSlotDialogData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20SignalSlotDialogData5clearEv(
    qdesigner_internal::SignalSlotDialogData *self) {
  self->clear();
}

//  qdesigner_internal::SignalSlotDialogData::~SignalSlotDialogData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20SignalSlotDialogDataD1Ev(
    qdesigner_internal::SignalSlotDialogData *self) {
  delete self;
}
