//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qbuttongroup_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(buttongroup)
#if QT_CONFIG(buttongroup)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qbuttongroup.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qbuttongroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qbuttongroup_p.h>
#include <QtWidgets/private/qabstractbutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qbuttongroup.cpp, line 12, as _ZN19QButtonGroupPrivate19detectCheckedButtonEv
inline void QButtonGroupPrivate::detectCheckedButton()
{
    QAbstractButton *previous = checkedButton;
    checkedButton = nullptr;
    if (exclusive)
        return;
    for (int i = 0; i < buttonList.size(); i++) {
        if (buttonList.at(i) != previous && buttonList.at(i)->isChecked()) {
            checkedButton = buttonList.at(i);
            return;
        }
    }
}
//  -----------------------------------------------------------------------

//  QButtonGroup *QButtonGroupPrivate::q_func()
extern "C" Q_DECL_EXPORT
QButtonGroup *ritual_ZN19QButtonGroupPrivate6q_funcEv(
    QButtonGroupPrivate *self) {
  return self->q_func();
}

//  const QButtonGroup *QButtonGroupPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QButtonGroup *ritual_ZNK19QButtonGroupPrivate6q_funcEv(
    const QButtonGroupPrivate *self) {
  return self->q_func();
}

//  QButtonGroupPrivate::QButtonGroupPrivate()
extern "C" Q_DECL_EXPORT
QButtonGroupPrivate *ritual_ZN19QButtonGroupPrivateC1Ev() {
  return new QButtonGroupPrivate();
}

//  void QButtonGroupPrivate::detectCheckedButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QButtonGroupPrivate19detectCheckedButtonEv(
    QButtonGroupPrivate *self) {
  self->detectCheckedButton();
}

#endif  // QT_CONFIG(buttongroup)
#endif  // QT_CONFIG(buttongroup)
