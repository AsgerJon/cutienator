//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/newactiondialog_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/newactiondialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/newactiondialog_p.h>
#include <QtDesigner/private/richtexteditor_p.h>
#include <QtDesigner/private/actioneditor_p.h>
#include <QtDesigner/private/formwindowbase_p.h>
#include <QtDesigner/private/qdesigner_utils_p.h>
#include <QtDesigner/private/iconloader_p.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtCore/QMetaEnum>
#include <QtWidgets/qpushbutton.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/newactiondialog.cpp, line 25, as _ZNK18qdesigner_internal10ActionData7compareERKS0_
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline unsigned ActionData::compare(const ActionData &rhs) const
{
    unsigned rc = 0;
    if (text != rhs.text)
        rc |= TextChanged;
    if (name != rhs.name)
        rc |= NameChanged;
    if (toolTip != rhs.toolTip)
        rc |= ToolTipChanged ;
    if (icon != rhs.icon)
        rc |= IconChanged ;
    if (checkable != rhs.checkable)
        rc |= CheckableChanged;
    if (keysequence != rhs.keysequence)
        rc |= KeysequenceChanged ;
    if (menuRole.value != rhs.menuRole.value)
        rc |= MenuRoleChanged ;
    return rc;
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  unsigned int qdesigner_internal::ActionData::compare(const ActionData
//      &rhs) const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK18qdesigner_internal10ActionData7compareERKS0_(
    const qdesigner_internal::ActionData *self,
    const qdesigner_internal::ActionData *rhs) {
  return self->compare(*rhs);
}

//  bool operator==(const ActionData &lhs, const ActionData &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_10ActionDataES2_(
    const qdesigner_internal::ActionData *lhs,
    const qdesigner_internal::ActionData *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ActionData &lhs, const ActionData &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_10ActionDataES2_(
    const qdesigner_internal::ActionData *lhs,
    const qdesigner_internal::ActionData *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::ActionData::~ActionData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal10ActionDataD1Ev(
    qdesigner_internal::ActionData *self) {
  delete self;
}
