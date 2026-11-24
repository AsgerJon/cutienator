//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpalette_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpalette_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPalettePrivate::QPalettePrivate()
extern "C" Q_DECL_EXPORT
QPalettePrivate *ritual_ZN15QPalettePrivateC1Ev() {
  return new QPalettePrivate();
}

//  QPalette::ResolveMask
//      QPalettePrivate::colorRoleOffset(QPalette::ColorGroup colorGroup)
extern "C" Q_DECL_EXPORT
QPalette::ResolveMask ritual_ZN15QPalettePrivate15colorRoleOffsetEN8QPalette10ColorGroupE(
    QPalette::ColorGroup colorGroup) {
  return QPalettePrivate::colorRoleOffset(colorGroup);
}

//  QPalette::ResolveMask QPalettePrivate::bitPosition(QPalette::ColorGroup
//      colorGroup, QPalette::ColorRole colorRole)
extern "C" Q_DECL_EXPORT
QPalette::ResolveMask ritual_ZN15QPalettePrivate11bitPositionEN8QPalette10ColorGroupENS0_9ColorRoleE(
    QPalette::ColorGroup colorGroup,
    QPalette::ColorRole colorRole) {
  return QPalettePrivate::bitPosition(colorGroup, colorRole);
}

//  QPalettePrivate::~QPalettePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPalettePrivateD1Ev(QPalettePrivate *self) {
  delete self;
}
