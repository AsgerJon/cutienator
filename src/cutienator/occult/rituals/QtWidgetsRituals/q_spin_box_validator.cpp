//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractspinbox_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractspinbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qplatformdefs.h>
#ifdef Q_OS_WASM
# include <QtCore/private/qstdweb_p.h>
#endif
#include <QtWidgets/private/qabstractspinbox_p.h>
#include <QtWidgets/private/qapplication_p.h>
#if QT_CONFIG(datetimeparser)
#include <QtCore/private/qdatetimeparser_p.h>
#endif
#include <QtWidgets/private/qlineedit_p.h>
#include <QtWidgets/qabstractspinbox.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qstylehints.h>
#include <QtGui/qclipboard.h>
#include <QtCore/qdatetime.h>
#include <QtGui/qevent.h>
#include <QtCore/qloggingcategory.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtWidgets/qstylepainter.h>
#if QT_CONFIG(accessibility)
# include <QtGui/qaccessible.h>
#endif
#include <QtCore/qpointer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1915, as _ZNK17QSpinBoxValidator8validateER7QStringRi
inline QValidator::State QSpinBoxValidator::validate(QString &input, int &pos) const
{
    if (dptr->specialValueText.size() > 0 && input == dptr->specialValueText)
        return QValidator::Acceptable;

    if (!dptr->prefix.isEmpty() && !input.startsWith(dptr->prefix)) {
        input.prepend(dptr->prefix);
        pos += dptr->prefix.size();
    }

    if (!dptr->suffix.isEmpty() && !input.endsWith(dptr->suffix))
        input.append(dptr->suffix);

    return qptr->validate(input, pos);
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1935, as _ZNK17QSpinBoxValidator5fixupER7QString
inline void QSpinBoxValidator::fixup(QString &input) const
{
    qptr->fixup(input);
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1902, as _ZN17QSpinBoxValidatorC1EP16QAbstractSpinBoxP23QAbstractSpinBoxPrivate
inline QSpinBoxValidator::QSpinBoxValidator(QAbstractSpinBox *qp, QAbstractSpinBoxPrivate *dp)
    : QValidator(qp), qptr(qp), dptr(dp)
{
    setObjectName("qt_spinboxvalidator"_L1);
}
//  -----------------------------------------------------------------------

//  QSpinBoxValidator::QSpinBoxValidator(QAbstractSpinBox *qptr,
//      QAbstractSpinBoxPrivate *dptr)
extern "C" Q_DECL_EXPORT
QSpinBoxValidator *ritual_ZN17QSpinBoxValidatorC1EP16QAbstractSpinBoxP23QAbstractSpinBoxPrivate(
    QAbstractSpinBox *qptr,
    QAbstractSpinBoxPrivate *dptr) {
  return new QSpinBoxValidator(qptr, dptr);
}

//  QValidator::State QSpinBoxValidator::validate(QString &input, int &a1)
//      const
extern "C" Q_DECL_EXPORT
QValidator::State ritual_ZNK17QSpinBoxValidator8validateER7QStringRi(
    const QSpinBoxValidator *self,
    QString *input,
    int *a1) {
  return self->validate(*input, *a1);
}

//  void QSpinBoxValidator::fixup(QString &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QSpinBoxValidator5fixupER7QString(
    const QSpinBoxValidator *self,
    QString *a0) {
  self->fixup(*a0);
}

#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(spinbox)
