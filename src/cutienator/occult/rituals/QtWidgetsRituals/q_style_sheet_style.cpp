//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qstylesheetstyle_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(style_stylesheet)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qstylesheetstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qpalette.h>
#include <QtCore/qstring.h>
#include <QtGui/qfontmetrics.h>
#include <QtGui/qfont.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qicon.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qglobal.h>
#include <QtWidgets/private/qstylesheetstyle_p.h>
#if QT_CONFIG(style_stylesheet)
#include <QtGui/private/qcssutil_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qdir.h>
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#if QT_CONFIG(menubar)
#include <QtWidgets/qmenubar.h>
#endif
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#if QT_CONFIG(textedit)
#include <QtWidgets/qtextedit.h>
#include <QtWidgets/qplaintextedit.h>
#endif
#include <QtWidgets/private/qwindowsstyle_p.h>
#if QT_CONFIG(combobox)
#include <QtWidgets/qcombobox.h>
#endif
#include <QtGui/private/qcssparser_p.h>
#include <QtGui/private/qmath_p.h>
#include <QtWidgets/qabstractscrollarea.h>
#include <QtWidgets/private/qabstractscrollarea_p.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/private/qtooltip_p.h>
#endif
#include <QtCore/qshareddata.h>
#if QT_CONFIG(toolbutton)
#include <QtWidgets/qtoolbutton.h>
#endif
#if QT_CONFIG(scrollbar)
#include <QtWidgets/qscrollbar.h>
#endif
#if QT_CONFIG(abstractslider)
#include <QtWidgets/qabstractslider.h>
#endif
#include <QtCore/qstring.h>
#include <QtCore/qfile.h>
#if QT_CONFIG(checkbox)
#include <QtWidgets/qcheckbox.h>
#endif
#if QT_CONFIG(itemviews)
#include <QtWidgets/qheaderview.h>
#endif
#include <QtWidgets/private/qwindowsstyle_p_p.h>
#if QT_CONFIG(animation)
#include <QtWidgets/private/qstyleanimation_p.h>
#endif
#if QT_CONFIG(tabbar)
#include <QtWidgets/private/qtabbar_p.h>
#endif
#include <QtCore/QMetaProperty>
#if QT_CONFIG(mainwindow)
#include <QtWidgets/qmainwindow.h>
#endif
#if QT_CONFIG(dockwidget)
#include <QtWidgets/qdockwidget.h>
#endif
#if QT_CONFIG(mdiarea)
#include <QtWidgets/qmdisubwindow.h>
#endif
#if QT_CONFIG(dialog)
#include <QtWidgets/qdialog.h>
#endif
#include <QtWidgets/private/qwidget_p.h>
#if QT_CONFIG(spinbox)
#include <QtWidgets/QAbstractSpinBox>
#endif
#if QT_CONFIG(label)
#include <QtWidgets/QLabel>
#endif
#include <QtWidgets/qdrawutil.h>
#include <QtWidgets/private/qstylehelper_p.h>
#include <limits.h>
#if QT_CONFIG(toolbar)
#include <QtWidgets/qtoolbar.h>
#endif
#if QT_CONFIG(pushbutton)
#include <QtWidgets/qpushbutton.h>
#endif
#include <QtGui/qpainterpath.h>
#include <QtGui/qpainterstateguard.h>
#include <QtGui/qscreen.h>
#include <QtCore/private/qduplicatetracker_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/styles/qstylesheetstyle.cpp, line 4563, as _ZNK16QStyleSheetStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap
#if QT_CONFIG(style_stylesheet)
inline void QStyleSheetStyle::drawItemPixmap(QPainter *p, const QRect &rect, int alignment, const
                                  QPixmap &pixmap) const
{
    baseStyle()->drawItemPixmap(p, rect, alignment, pixmap);
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 4569, as _ZNK16QStyleSheetStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE
#if QT_CONFIG(style_stylesheet)
inline void QStyleSheetStyle::drawItemText(QPainter *painter, const QRect& rect, int alignment, const QPalette &pal,
                                bool enabled, const QString& text, QPalette::ColorRole textRole) const
{
    baseStyle()->drawItemText(painter, rect, alignment, pal, enabled, text, textRole);
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 4950, as _ZNK16QStyleSheetStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption
#if QT_CONFIG(style_stylesheet)
inline QPixmap QStyleSheetStyle::generatedIconPixmap(QIcon::Mode iconMode, const QPixmap& pixmap,
                                          const QStyleOption *option) const
{
    return baseStyle()->generatedIconPixmap(iconMode, pixmap, option);
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 5008, as _ZNK16QStyleSheetStyle14itemPixmapRectERK5QRectiRK7QPixmap
#if QT_CONFIG(style_stylesheet)
inline QRect QStyleSheetStyle::itemPixmapRect(const QRect &rect, int alignment, const QPixmap &pixmap) const
{
    return baseStyle()->itemPixmapRect(rect, alignment, pixmap);
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 5013, as _ZNK16QStyleSheetStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString
#if QT_CONFIG(style_stylesheet)
inline QRect QStyleSheetStyle::itemTextRect(const QFontMetrics &metrics, const QRect& rect, int alignment,
                                 bool enabled, const QString& text) const
{
    return baseStyle()->itemTextRect(metrics, rect, alignment, enabled, text);
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 2976, as _ZN16QStyleSheetStyle6polishEP12QApplication
#if QT_CONFIG(style_stylesheet)
inline void QStyleSheetStyle::polish(QApplication *app)
{
    baseStyle()->polish(app);
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 5681, as _ZNK16QStyleSheetStyle15standardPaletteEv
#if QT_CONFIG(style_stylesheet)
inline QPalette QStyleSheetStyle::standardPalette() const
{
    return baseStyle()->standardPalette();
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 5701, as _ZNK16QStyleSheetStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget
#if QT_CONFIG(style_stylesheet)
inline int QStyleSheetStyle::layoutSpacing(QSizePolicy::ControlType control1, QSizePolicy::ControlType control2,
                          Qt::Orientation orientation, const QStyleOption *option,
                          const QWidget *widget) const
{
    return baseStyle()->layoutSpacing(control1, control2, orientation, option, widget);
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 6516, as _ZNK16QStyleSheetStyle14saveWidgetFontEP7QWidgetRK5QFont
#if QT_CONFIG(style_stylesheet)
inline void QStyleSheetStyle::saveWidgetFont(QWidget* w, const QFont& font) const
{
    w->setProperty("_q_styleSheetWidgetFont", font);
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 6521, as _ZNK16QStyleSheetStyle15clearWidgetFontEP7QWidget
#if QT_CONFIG(style_stylesheet)
inline void QStyleSheetStyle::clearWidgetFont(QWidget* w) const
{
    w->setProperty("_q_styleSheetWidgetFont", QVariant());
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 6464, as _ZN16QStyleSheetStyle5eventEP6QEvent
#if QT_CONFIG(style_stylesheet)
inline bool QStyleSheetStyle::event(QEvent *e)
{
    return (baseStyle()->event(e) && e->isAccepted()) || ParentStyle::event(e);
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 6547, as _ZN16QStyleSheetStyle16resolveAlignmentEN2Qt15LayoutDirectionE6QFlagsINS0_13AlignmentFlagEE
#if QT_CONFIG(style_stylesheet)
inline Qt::Alignment QStyleSheetStyle::resolveAlignment(Qt::LayoutDirection layDir, Qt::Alignment src)
{
    if (layDir == Qt::LeftToRight || src & Qt::AlignAbsolute)
        return src;

    if (src & Qt::AlignLeft) {
        src &= ~Qt::AlignLeft;
        src |= Qt::AlignRight;
    } else if (src & Qt::AlignRight) {
        src &= ~Qt::AlignRight;
        src |= Qt::AlignLeft;
    }
    src |= Qt::AlignAbsolute;
    return src;
}
#endif  // QT_CONFIG(style_stylesheet)

//  from src/widgets/styles/qstylesheetstyle.cpp, line 6577, as _ZN16QStyleSheetStyle10loadPixmapERK7QStringPK7QObject
#if QT_CONFIG(style_stylesheet)
inline QPixmap QStyleSheetStyle::loadPixmap(const QString &fileName, const QObject *context)
{
    if (fileName.isEmpty())
        return {};

    qreal ratio = -1.0;
    if (const QWidget *widget = qobject_cast<const QWidget *>(context)) {
        if (QScreen *screen = QApplication::screenAt(widget->mapToGlobal(QPoint(0, 0))))
            ratio = screen->devicePixelRatio();
    }

    if (ratio < 0) {
        if (const QApplication *app = qApp)
            ratio = app->devicePixelRatio();
        else
            ratio = 1.0;
    }

    qreal sourceDevicePixelRatio = 1.0;
    QString resolvedFileName = qt_findAtNxFile(fileName, ratio, &sourceDevicePixelRatio);
    QPixmap pixmap(resolvedFileName);
    pixmap.setDevicePixelRatio(sourceDevicePixelRatio);
    return pixmap;
}
#endif  // QT_CONFIG(style_stylesheet)
//  -----------------------------------------------------------------------

//  A QStyleSheetStyle that Python can take functions over in. Every QStyleSheetStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef void (*CuteQStyleSheetStyleCall0)(const void *, int, const QStyleOptionComplex *, QPainter *, const QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef void (*CuteQStyleSheetStyleCall1)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef void (*CuteQStyleSheetStyleCall2)(const void *, QPainter *, const QRect *, int, const QPixmap *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef void (*CuteQStyleSheetStyleCall3)(const void *, QPainter *, const QRect *, int, const QPalette *, bool, const QString *, int, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef void (*CuteQStyleSheetStyleCall4)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef const QPixmap * (*CuteQStyleSheetStyleCall5)(const void *, int, const QPixmap *, const QStyleOption *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef int (*CuteQStyleSheetStyleCall6)(const void *, int, const QStyleOptionComplex *, const QPoint *, const QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef const QRect * (*CuteQStyleSheetStyleCall7)(const void *, const QRect *, int, const QPixmap *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef const QRect * (*CuteQStyleSheetStyleCall8)(const void *, const QFontMetrics *, const QRect *, int, bool, const QString *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef int (*CuteQStyleSheetStyleCall9)(const void *, int, const QStyleOption *, const QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef void (*CuteQStyleSheetStyleCall10)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef void (*CuteQStyleSheetStyleCall11)(const void *, QApplication *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef const QSize * (*CuteQStyleSheetStyleCall12)(const void *, int, const QStyleOption *, const QSize *, const QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef const QPalette * (*CuteQStyleSheetStyleCall13)(const void *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef const QIcon * (*CuteQStyleSheetStyleCall14)(const void *, int, const QStyleOption *, const QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef const QPixmap * (*CuteQStyleSheetStyleCall15)(const void *, int, const QStyleOption *, const QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef int (*CuteQStyleSheetStyleCall16)(const void *, int, int, int, const QStyleOption *, const QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef int (*CuteQStyleSheetStyleCall17)(const void *, int, const QStyleOption *, const QWidget *, QStyleHintReturn *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef const QRect * (*CuteQStyleSheetStyleCall18)(const void *, int, const QStyleOption *, const QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef const QRect * (*CuteQStyleSheetStyleCall19)(const void *, int, const QStyleOptionComplex *, int, const QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef void (*CuteQStyleSheetStyleCall20)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef void (*CuteQStyleSheetStyleCall21)(const void *, QApplication *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
typedef bool (*CuteQStyleSheetStyleCall22)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(style_windows)
typedef bool (*CuteQStyleSheetStyleCall23)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(style_windows)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleSheetStyleCall24)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleSheetStyleCall25)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleSheetStyleCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleSheetStyleCall27)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleSheetStyleCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQStyleSheetStyle : public QStyleSheetStyle {
public:
  using QStyleSheetStyle::QStyleSheetStyle;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle18drawComplexControlENS_14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle11drawControlENS_14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle13drawPrimitiveENS_16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle21hitTestComplexControlENS_14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle11pixelMetricENS_11PixelMetricEPK12QStyleOptionPK7QWidget")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZN6QStyle6polishEP7QWidget")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZN6QStyle6polishEP12QApplication")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle16sizeFromContentsENS_12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle15standardPaletteEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle12standardIconENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle14standardPixmapENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle9styleHintENS_9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle14subElementRectENS_10SubElementEPK12QStyleOptionPK7QWidget")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZNK6QStyle14subControlRectENS_14ComplexControlEPK19QStyleOptionComplexNS_10SubControlEPK7QWidget")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP7QWidget")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP12QApplication")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(style_windows)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(style_windows)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  void QStyleSheetStyle::drawComplexControl(ComplexControl cc, const
  //      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
  void drawComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQStyleSheetStyleCall0 call = reinterpret_cast<CuteQStyleSheetStyleCall0>(taken[0]);
      call(this, static_cast<int>(cc), opt, p, w, &handled);
      if (handled) return;
    }
    QStyleSheetStyle::drawComplexControl(cc, opt, p, w);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  void QStyleSheetStyle::drawControl(ControlElement element, const
  //      QStyleOption *opt, QPainter *p, const QWidget *w) const
  void drawControl(
      QStyle::ControlElement element,
      const QStyleOption *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQStyleSheetStyleCall1 call = reinterpret_cast<CuteQStyleSheetStyleCall1>(taken[1]);
      call(this, static_cast<int>(element), opt, p, w, &handled);
      if (handled) return;
    }
    QStyleSheetStyle::drawControl(element, opt, p, w);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  void QStyleSheetStyle::drawItemPixmap(QPainter *painter, const QRect
  //      &rect, int alignment, const QPixmap &pixmap) const
  void drawItemPixmap(
      QPainter *painter,
      const QRect &rect,
      int alignment,
      const QPixmap &pixmap) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQStyleSheetStyleCall2 call = reinterpret_cast<CuteQStyleSheetStyleCall2>(taken[2]);
      call(this, painter, &rect, alignment, &pixmap, &handled);
      if (handled) return;
    }
    QStyleSheetStyle::drawItemPixmap(painter, rect, alignment, pixmap);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  void QStyleSheetStyle::drawItemText(QPainter *painter, const QRect
  //      &rect, int alignment, const QPalette &pal, bool enabled, const
  //      QString &text, QPalette::ColorRole textRole) const
  void drawItemText(
      QPainter *painter,
      const QRect &rect,
      int alignment,
      const QPalette &pal,
      bool enabled,
      const QString &text,
      QPalette::ColorRole textRole) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQStyleSheetStyleCall3 call = reinterpret_cast<CuteQStyleSheetStyleCall3>(taken[3]);
      call(this, painter, &rect, alignment, &pal, enabled, &text, static_cast<int>(textRole), &handled);
      if (handled) return;
    }
    QStyleSheetStyle::drawItemText(painter, rect, alignment, pal, enabled, text, textRole);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  void QStyleSheetStyle::drawPrimitive(PrimitiveElement pe, const
  //      QStyleOption *opt, QPainter *p, const QWidget *w) const
  void drawPrimitive(
      QStyle::PrimitiveElement pe,
      const QStyleOption *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQStyleSheetStyleCall4 call = reinterpret_cast<CuteQStyleSheetStyleCall4>(taken[4]);
      call(this, static_cast<int>(pe), opt, p, w, &handled);
      if (handled) return;
    }
    QStyleSheetStyle::drawPrimitive(pe, opt, p, w);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  QPixmap QStyleSheetStyle::generatedIconPixmap(QIcon::Mode iconMode,
  //      const QPixmap &pixmap, const QStyleOption *option) const
  QPixmap generatedIconPixmap(
      QIcon::Mode iconMode,
      const QPixmap &pixmap,
      const QStyleOption *option) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQStyleSheetStyleCall5 call = reinterpret_cast<CuteQStyleSheetStyleCall5>(taken[5]);
      const QPixmap * given = call(this, static_cast<int>(iconMode), &pixmap, option, &handled);
      if (handled && given) return *given;
    }
    return QStyleSheetStyle::generatedIconPixmap(iconMode, pixmap, option);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  SubControl QStyleSheetStyle::hitTestComplexControl(ComplexControl cc,
  //      const QStyleOptionComplex *opt, const QPoint &pt, const QWidget
  //      *w) const
  QStyle::SubControl hitTestComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      const QPoint &pt,
      const QWidget *w) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQStyleSheetStyleCall6 call = reinterpret_cast<CuteQStyleSheetStyleCall6>(taken[6]);
      int given = call(this, static_cast<int>(cc), opt, &pt, w, &handled);
      if (handled) return static_cast<QStyle::SubControl>(given);
    }
    return QStyleSheetStyle::hitTestComplexControl(cc, opt, pt, w);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  QRect QStyleSheetStyle::itemPixmapRect(const QRect &rect, int
  //      alignment, const QPixmap &pixmap) const
  QRect itemPixmapRect(
      const QRect &rect,
      int alignment,
      const QPixmap &pixmap) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQStyleSheetStyleCall7 call = reinterpret_cast<CuteQStyleSheetStyleCall7>(taken[7]);
      const QRect * given = call(this, &rect, alignment, &pixmap, &handled);
      if (handled && given) return *given;
    }
    return QStyleSheetStyle::itemPixmapRect(rect, alignment, pixmap);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  QRect QStyleSheetStyle::itemTextRect(const QFontMetrics &metrics,
  //      const QRect &rect, int alignment, bool enabled, const QString
  //      &text) const
  QRect itemTextRect(
      const QFontMetrics &metrics,
      const QRect &rect,
      int alignment,
      bool enabled,
      const QString &text) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQStyleSheetStyleCall8 call = reinterpret_cast<CuteQStyleSheetStyleCall8>(taken[8]);
      const QRect * given = call(this, &metrics, &rect, alignment, enabled, &text, &handled);
      if (handled && given) return *given;
    }
    return QStyleSheetStyle::itemTextRect(metrics, rect, alignment, enabled, text);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  int QStyleSheetStyle::pixelMetric(PixelMetric metric, const
  //      QStyleOption *option, const QWidget *widget) const
  int pixelMetric(
      QStyle::PixelMetric metric,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQStyleSheetStyleCall9 call = reinterpret_cast<CuteQStyleSheetStyleCall9>(taken[9]);
      int given = call(this, static_cast<int>(metric), option, widget, &handled);
      if (handled) return given;
    }
    return QStyleSheetStyle::pixelMetric(metric, option, widget);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  void QStyleSheetStyle::polish(QWidget *widget)
  void polish(QWidget *widget) override {
    if (taken[10]) {
      int handled = 0;
      CuteQStyleSheetStyleCall10 call = reinterpret_cast<CuteQStyleSheetStyleCall10>(taken[10]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QStyleSheetStyle::polish(widget);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  void QStyleSheetStyle::polish(QApplication *app)
  void polish(QApplication *app) override {
    if (taken[11]) {
      int handled = 0;
      CuteQStyleSheetStyleCall11 call = reinterpret_cast<CuteQStyleSheetStyleCall11>(taken[11]);
      call(this, app, &handled);
      if (handled) return;
    }
    QStyleSheetStyle::polish(app);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  QSize QStyleSheetStyle::sizeFromContents(ContentsType ct, const
  //      QStyleOption *opt, const QSize &contentsSize, const QWidget
  //      *widget) const
  QSize sizeFromContents(
      QStyle::ContentsType ct,
      const QStyleOption *opt,
      const QSize &contentsSize,
      const QWidget *widget) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQStyleSheetStyleCall12 call = reinterpret_cast<CuteQStyleSheetStyleCall12>(taken[12]);
      const QSize * given = call(this, static_cast<int>(ct), opt, &contentsSize, widget, &handled);
      if (handled && given) return *given;
    }
    return QStyleSheetStyle::sizeFromContents(ct, opt, contentsSize, widget);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  QPalette QStyleSheetStyle::standardPalette() const
  QPalette standardPalette() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQStyleSheetStyleCall13 call = reinterpret_cast<CuteQStyleSheetStyleCall13>(taken[13]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QStyleSheetStyle::standardPalette();
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  QIcon QStyleSheetStyle::standardIcon(StandardPixmap standardIcon,
  //      const QStyleOption *opt, const QWidget *widget) const
  QIcon standardIcon(
      QStyle::StandardPixmap standardIcon,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQStyleSheetStyleCall14 call = reinterpret_cast<CuteQStyleSheetStyleCall14>(taken[14]);
      const QIcon * given = call(this, static_cast<int>(standardIcon), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return QStyleSheetStyle::standardIcon(standardIcon, opt, widget);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  QPixmap QStyleSheetStyle::standardPixmap(StandardPixmap
  //      standardPixmap, const QStyleOption *option, const QWidget *w)
  //      const
  QPixmap standardPixmap(
      QStyle::StandardPixmap standardPixmap,
      const QStyleOption *option,
      const QWidget *w) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQStyleSheetStyleCall15 call = reinterpret_cast<CuteQStyleSheetStyleCall15>(taken[15]);
      const QPixmap * given = call(this, static_cast<int>(standardPixmap), option, w, &handled);
      if (handled && given) return *given;
    }
    return QStyleSheetStyle::standardPixmap(standardPixmap, option, w);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  int QStyleSheetStyle::layoutSpacing(QSizePolicy::ControlType
  //      control1, QSizePolicy::ControlType control2, Qt::Orientation
  //      orientation, const QStyleOption *option, const QWidget *widget)
  //      const
  int layoutSpacing(
      QSizePolicy::ControlType control1,
      QSizePolicy::ControlType control2,
      Qt::Orientation orientation,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQStyleSheetStyleCall16 call = reinterpret_cast<CuteQStyleSheetStyleCall16>(taken[16]);
      int given = call(this, static_cast<int>(control1), static_cast<int>(control2), static_cast<int>(orientation), option, widget, &handled);
      if (handled) return given;
    }
    return QStyleSheetStyle::layoutSpacing(control1, control2, orientation, option, widget);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  int QStyleSheetStyle::styleHint(StyleHint sh, const QStyleOption
  //      *opt, const QWidget *w, QStyleHintReturn *shret) const
  int styleHint(
      QStyle::StyleHint sh,
      const QStyleOption *opt,
      const QWidget *w,
      QStyleHintReturn *shret) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQStyleSheetStyleCall17 call = reinterpret_cast<CuteQStyleSheetStyleCall17>(taken[17]);
      int given = call(this, static_cast<int>(sh), opt, w, shret, &handled);
      if (handled) return given;
    }
    return QStyleSheetStyle::styleHint(sh, opt, w, shret);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  QRect QStyleSheetStyle::subElementRect(SubElement r, const
  //      QStyleOption *opt, const QWidget *widget) const
  QRect subElementRect(
      QStyle::SubElement r,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQStyleSheetStyleCall18 call = reinterpret_cast<CuteQStyleSheetStyleCall18>(taken[18]);
      const QRect * given = call(this, static_cast<int>(r), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return QStyleSheetStyle::subElementRect(r, opt, widget);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  QRect QStyleSheetStyle::subControlRect(ComplexControl cc, const
  //      QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const
  QRect subControlRect(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      QStyle::SubControl sc,
      const QWidget *w) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQStyleSheetStyleCall19 call = reinterpret_cast<CuteQStyleSheetStyleCall19>(taken[19]);
      const QRect * given = call(this, static_cast<int>(cc), opt, static_cast<int>(sc), w, &handled);
      if (handled && given) return *given;
    }
    return QStyleSheetStyle::subControlRect(cc, opt, sc, w);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  void QStyleSheetStyle::unpolish(QWidget *widget)
  void unpolish(QWidget *widget) override {
    if (taken[20]) {
      int handled = 0;
      CuteQStyleSheetStyleCall20 call = reinterpret_cast<CuteQStyleSheetStyleCall20>(taken[20]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QStyleSheetStyle::unpolish(widget);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  void QStyleSheetStyle::unpolish(QApplication *app)
  void unpolish(QApplication *app) override {
    if (taken[21]) {
      int handled = 0;
      CuteQStyleSheetStyleCall21 call = reinterpret_cast<CuteQStyleSheetStyleCall21>(taken[21]);
      call(this, app, &handled);
      if (handled) return;
    }
    QStyleSheetStyle::unpolish(app);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(style_windows)
#if QT_CONFIG(style_stylesheet)
  //  bool QStyleSheetStyle::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[22]) {
      int handled = 0;
      CuteQStyleSheetStyleCall22 call = reinterpret_cast<CuteQStyleSheetStyleCall22>(taken[22]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QStyleSheetStyle::event(e);
  }
#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(style_windows)
  //  bool QWindowsStyle::eventFilter(QObject *o, QEvent *e)
  bool eventFilter(QObject *o, QEvent *e) override {
    if (taken[23]) {
      int handled = 0;
      CuteQStyleSheetStyleCall23 call = reinterpret_cast<CuteQStyleSheetStyleCall23>(taken[23]);
      bool given = call(this, o, e, &handled);
      if (handled) return given;
    }
    return QWindowsStyle::eventFilter(o, e);
  }
#endif  // QT_CONFIG(style_windows)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQStyleSheetStyleCall24 call = reinterpret_cast<CuteQStyleSheetStyleCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQStyleSheetStyleCall25 call = reinterpret_cast<CuteQStyleSheetStyleCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQStyleSheetStyleCall26 call = reinterpret_cast<CuteQStyleSheetStyleCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[27]) {
      int handled = 0;
      CuteQStyleSheetStyleCall27 call = reinterpret_cast<CuteQStyleSheetStyleCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQStyleSheetStyleCall28 call = reinterpret_cast<CuteQStyleSheetStyleCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QStyleSheetStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QStyleSheetStyle10metaObjectEv(
    const QStyleSheetStyle *self) {
  return self->metaObject();
}

//  void QStyleSheetStyle::drawItemPixmap(QPainter *painter, const QRect
//      &rect, int alignment, const QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QStyleSheetStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap(
    const QStyleSheetStyle *self,
    QPainter *painter,
    const QRect *rect,
    int alignment,
    const QPixmap *pixmap) {
  self->drawItemPixmap(painter, *rect, alignment, *pixmap);
}

//  void QStyleSheetStyle::drawItemText(QPainter *painter, const QRect &rect,
//      int alignment, const QPalette &pal, bool enabled, const QString
//      &text, QPalette::ColorRole textRole) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QStyleSheetStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE(
    const QStyleSheetStyle *self,
    QPainter *painter,
    const QRect *rect,
    int alignment,
    const QPalette *pal,
    bool enabled,
    const QString *text,
    QPalette::ColorRole textRole) {
  self->drawItemText(
      painter,
      *rect,
      alignment,
      *pal,
      enabled,
      *text,
      textRole);
}

//  QPixmap QStyleSheetStyle::generatedIconPixmap(QIcon::Mode iconMode, const
//      QPixmap &pixmap, const QStyleOption *option) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK16QStyleSheetStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption(
    const QStyleSheetStyle *self,
    QIcon::Mode iconMode,
    const QPixmap *pixmap,
    const QStyleOption *option) {
  return new QPixmap(self->generatedIconPixmap(iconMode, *pixmap, option));
}

//  QRect QStyleSheetStyle::itemPixmapRect(const QRect &rect, int alignment,
//      const QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QStyleSheetStyle14itemPixmapRectERK5QRectiRK7QPixmap(
    const QStyleSheetStyle *self,
    const QRect *rect,
    int alignment,
    const QPixmap *pixmap) {
  return new QRect(self->itemPixmapRect(*rect, alignment, *pixmap));
}

//  QRect QStyleSheetStyle::itemTextRect(const QFontMetrics &metrics, const
//      QRect &rect, int alignment, bool enabled, const QString &text) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QStyleSheetStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString(
    const QStyleSheetStyle *self,
    const QFontMetrics *metrics,
    const QRect *rect,
    int alignment,
    bool enabled,
    const QString *text) {
  return new QRect(
      self->itemTextRect(
          *metrics,
          *rect,
          alignment,
          enabled,
          *text));
}

//  void QStyleSheetStyle::polish(QApplication *app)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QStyleSheetStyle6polishEP12QApplication(
    QStyleSheetStyle *self,
    QApplication *app) {
  self->polish(app);
}

//  QPalette QStyleSheetStyle::standardPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK16QStyleSheetStyle15standardPaletteEv(
    const QStyleSheetStyle *self) {
  return new QPalette(self->standardPalette());
}

//  int QStyleSheetStyle::layoutSpacing(QSizePolicy::ControlType control1,
//      QSizePolicy::ControlType control2, Qt::Orientation orientation, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QStyleSheetStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget(
    const QStyleSheetStyle *self,
    QSizePolicy::ControlType control1,
    QSizePolicy::ControlType control2,
    Qt::Orientation orientation,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->layoutSpacing(
      control1,
      control2,
      orientation,
      option,
      widget);
}

//  void QStyleSheetStyle::ref()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QStyleSheetStyle3refEv(QStyleSheetStyle *self) {
  self->ref();
}

//  void QStyleSheetStyle::deref()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QStyleSheetStyle5derefEv(QStyleSheetStyle *self) {
  self->deref();
}

#if QT_CONFIG(style_stylesheet)
//  void QStyleSheetStyle::saveWidgetFont(QWidget *w, const QFont &font)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QStyleSheetStyle14saveWidgetFontEP7QWidgetRK5QFont(
    const QStyleSheetStyle *self,
    QWidget *w,
    const QFont *font) {
  self->saveWidgetFont(w, *font);
}
#endif  // QT_CONFIG(style_stylesheet)

#if QT_CONFIG(style_stylesheet)
//  void QStyleSheetStyle::clearWidgetFont(QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QStyleSheetStyle15clearWidgetFontEP7QWidget(
    const QStyleSheetStyle *self,
    QWidget *w) {
  self->clearWidgetFont(w);
}
#endif  // QT_CONFIG(style_stylesheet)

//  bool QStyleSheetStyle::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QStyleSheetStyle5eventEP6QEvent(
    QStyleSheetStyle *self,
    QEvent *e) {
  return self->event(e);
}

#if QT_CONFIG(style_stylesheet)
//  Qt::Alignment QStyleSheetStyle::resolveAlignment(Qt::LayoutDirection a0,
//      Qt::Alignment a1)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QStyleSheetStyle16resolveAlignmentEN2Qt15LayoutDirectionE6QFlagsINS0_13AlignmentFlagEE(
    Qt::LayoutDirection a0,
    int a1) {
  return static_cast<int>(
      QStyleSheetStyle::resolveAlignment(
          a0,
          QFlags<Qt::AlignmentFlag>::fromInt(a1)).toInt());
}
#endif  // QT_CONFIG(style_stylesheet)

#if QT_CONFIG(style_stylesheet)
//  QPixmap QStyleSheetStyle::loadPixmap(const QString &fileName, const
//      QObject *context)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN16QStyleSheetStyle10loadPixmapERK7QStringPK7QObject(
    const QString *fileName,
    const QObject *context) {
  return new QPixmap(QStyleSheetStyle::loadPixmap(*fileName, context));
}
#endif  // QT_CONFIG(style_stylesheet)

//  a Python function taken by a CuteQStyleSheetStyle, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStyleSheetStyle(
    QStyleSheetStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStyleSheetStyle *>(self)->take(key, call);
}

#endif  // QT_CONFIG(style_stylesheet)
#endif  // QT_CONFIG(style_windows)
#endif  // QT_CONFIG(style_stylesheet)
