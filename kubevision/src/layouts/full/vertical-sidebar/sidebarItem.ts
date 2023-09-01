import {
    CopyIcon,
    LayoutDashboardIcon, 
    LoginIcon, 
    DashboardIcon, 
    ToolIcon
} from 'vue-tabler-icons';

export interface menu {
    header?: string;
    title?: string;
    icon?: any;
    to?: string;
    chip?: string;
    chipColor?: string;
    chipVariant?: string;
    chipIcon?: string;
    children?: menu[];
    disabled?: boolean;
    type?: string;
    subCaption?: string;
}

const sidebarItem: menu[] = [
    { header: 'Home' },
    {
        title: 'Dashboard',
        icon: LayoutDashboardIcon,
        to: '/'
    },
    { header: 'utilities' },
    {
        title: 'Clusters',
        icon: DashboardIcon,
        to: '/ui/clusters'
    },
    {
        title: 'Nodes',
        icon: CopyIcon,
        to: '/ui/nodes'
    },
    {
        title: 'Namespaces',
        icon: ToolIcon,
        to: '/ui/namespaces'
    },
    { header: 'auth' },
    {
        title: 'Login',
        icon: LoginIcon,
        to: '/auth/login'
    },
];

export default sidebarItem;
